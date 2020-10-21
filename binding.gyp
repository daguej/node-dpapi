{
  "targets": [
    {
      "target_name": "node-dpapi",
      "sources": [ "src/node-dpapi.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "include"
      ],
      'conditions': [
        ['OS == "win"', {
          "libraries": [
            "-lcrypt32.lib"
          ]
        }]
      ]
    }
  ]
}