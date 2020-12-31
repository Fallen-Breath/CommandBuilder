Command Builder
-------

A simple in development command builder for MCDReforged

Current it works as an plugin API of MCDReforged, so everything is inside a single file

Example Plugin: [LocationMarker](https://github.com/TISUnion/LocationMarker)

### Custom Argument

1. Create your custom argument class `MyArg`
2. Let `MyArg` inherit class `ArgumentNode`
3. Implement method `parse`. It returns a `ParseResult` storing the parsed value and char it has read. Raise a `IllegalArgument` error if it fails
4. done


### Custom Command Syntax Error

1. Create your custom error class `MyError`
2. Let `MyError inherit class `CommandSyntaxError`
3. done
