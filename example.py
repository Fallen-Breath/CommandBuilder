from command_builder import *


class Point(ArgumentNode):
	def parse(self, text):
		x, read_count_x = get_float(text)
		read_count_y = 0
		if x is not None:
			y, read_count_y = get_float(text[read_count_x:])
			if y is not None:
				return ParseResult((x, y), read_count_x + read_count_y)
		raise IllegalArgument('Illegal point', read_count_x + read_count_y)


if __name__ == '__main__':
	executor = Literal('test').\
		then(
			Literal('ping').run(lambda ctx: print('pong'))
		).\
		then(
			Literal('int').then(
				Integer('value').run(lambda ctx: print('ctx', ctx))
			)
		).\
		then(
			Integer('x').then(
				Float('y').then(
					Number('z').
						run(lambda ctx: print('pos=[{}, {}, {}]'.format(ctx['x'], ctx['y'], ctx['z'])))
				)
			)
		).\
		then(
			Literal('str').
				run(lambda ctx: print('no text')).
				then(
					Text('t1').run(lambda ctx: print('text1: ' + ctx['t1'])).
						then(
							GreedyText('t2').run(lambda ctx: print('text1: ' + ctx['t1'] + '; text2: ' + ctx['t2']))
						)
				)
		).\
		then(
			Literal('quote').
				then(
					QuotableText('qt').
						run(lambda ctx: print('quote text: {}'.format(ctx['qt']))).
						then(
							Number('num').run(lambda ctx: print('quote text: {}, number: {}'.format(ctx['qt'], ctx['num'])))
						)
				)
		).\
		then(
			Literal('point').
				then(
					Point('p').
						run(lambda ctx: print('Point={}'.format(ctx['p'])))
				)
		)
	while True:
		try:
			executor.execute(input())
		except Exception as e:
			print(e)
