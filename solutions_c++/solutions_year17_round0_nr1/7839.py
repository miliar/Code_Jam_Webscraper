#include <bits/stdc++.h>
using namespace std;

int len;
int pan_size;
int state[1050];
int op;
bool impossible;

void recurse_create(int index)
{
  if (index + pan_size > len)
  {
    for (int i = index; i < len; i++)
    {
      if (state[i] != 1)
      {
        impossible = true;
        break;
      }
    }
    return;
  }
  if (state[index] == 0)
  {
    op++;
    for (int i = index; i < (index + pan_size); i++)
    {
      state[i] = (state[i] + 1) % 2;
    }
  }
  return recurse_create(index + 1);
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; t++)
  {
    string s;
    cin >> s;
    len = s.length();
    cin >> pan_size;
    for (int i = 0; i < len; i++)
    {
      state[i] = (s[i] == '+') ? 1 : 0;
    }
    impossible = false;
    op = 0;
    recurse_create(0);
    if (impossible)
    {
      printf("Case #%d: IMPOSSIBLE\n", t + 1);
    }
    else
    {
      printf("Case #%d: %d\n", t + 1, op);
    }
  }
}