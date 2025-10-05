### Input data
Place your data in the `input.csv` file. The expected format is as follows:

```csv
No.,Date,Time
1,2025-09-23 19:42:17,3:21.17
2,2025-09-23 22:00:08,3:34.10
3,2025-09-23 22:05:05,3:03.52
...
```

[csTimer](https://csTimer.net) allows you to export data in a similar format:
<details>
<summary>See format</summary>

```csv
No.;Time;Comment;Scramble;Date;P.1
1;3:21.27;;"  R-- D++ R-- D-- R++ D-- R-- D++ R-- D++ U
  R++ D++ R++ D++ R++ D++ R-- D-- R++ D++ U
  R++ D-- R-- D-- R++ D++ R++ D++ R-- D++ U
  R++ D-- R++ D-- R-- D-- R-- D-- R++ D++ U
  R-- D++ R-- D++ R-- D++ R-- D++ R++ D++ U
  R-- D-- R-- D-- R++ D-- R++ D++ R-- D-- U'
  R++ D-- R-- D++ R++ D++ R-- D-- R++ D++ U
";2025-09-23 19:42:17;3:21.27
2;3:34.10;;"  R++ D++ R-- D-- R++ D++ R-- D++ R-- D++ U
  R-- D-- R++ D++ R++ D-- R-- D-- R++ D-- U'
  R-- D-- R-- D-- R-- D-- R-- D-- R-- D++ U
  R++ D++ R-- D-- R++ D-- R++ D-- R++ D-- U'
  R-- D-- R++ D++ R++ D++ R++ D++ R-- D-- U'
  R++ D++ R-- D-- R++ D-- R++ D++ R-- D-- U'
  R++ D-- R-- D++ R++ D-- R++ D++ R-- D-- U'
";2025-09-23 22:00:08;3:34.10
```

</details>

You can transform this output by manually replacing the first line with `No.,Date,Time`, replacing all semicolons with commas, and applying the following regex (e.g. in Sublime Text):
```regex
([0-9]{1,2});(.+);.*;".+\n.+\n.+\n.+\n.+\n.+\n.+\n";(.+);.+
```
Into:
```regex
$1,$3,$2
```
This regex is untested when solves are supplied with comments and you might need to tweak it.