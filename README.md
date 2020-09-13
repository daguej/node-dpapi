# node-dpapi
Node native module to encrypt/decrypt data. On Windows, it uses DPAPI

## API:
```typescript
function protectData(
    userData: Uint8Array,
    optionalEntropy: Uint8Array,
    scope: "CurrentUser" | "LocalMachine"
): Uint8Array;

function unprotectData(
    encryptedData: Uint8Array,
    optionalEntropy: Uint8Array,
    scope: "CurrentUser" | "LocalMachine"
): Uint8Array;
```

## Example:
```javascript
import * as dpapi from "node-dpapi";

const buffer = Buffer.from("Hello world", "utf-8");

const encrypted = dpapi.protectData(buffer, null, "CurrentUser");
const decrypted = dpapi.unprotectData(encrypted, null, "CurrentUser");
```

## FAQ:
Q: Does this work on all platforms?

A: Currently it just works on Windows

Q: This isn't working with Electorn, and I'm getting errors

A: Take look at this [documentation](https://www.electronjs.org/docs/tutorial/using-native-node-modules) Use `electron-rebuild` to compile against the right version

## Publish note
This package originates from [bradhugh/node-dpapi](https://github.com/bradhugh/node-dpapi), but he [did not publish it to npm](https://github.com/bradhugh/node-dpapi/issues/1).  [I](https://github.com/daguej) have taken the liberty of publishing this package so it may be used as a dependency.
