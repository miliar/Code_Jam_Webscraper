#include <stdio.h>
#include <queue>
#include <functional>

using namespace std;

priority_queue<int> q1; 
priority_queue<int> q2;
int n, s, k;
int ans1, ans2;

void insert(int p1, int p2)
{
  q1.push(p1);
  q2.push(p2);
  while(k != 0)
  {
    k--;
    p1 = q1.top();
    q1.pop();
    p2 = q2.top();
    q2.pop();

    if (k == 0)
    {
      ans1 = p1;
      ans2 = p2;
    }

    if (p1 != 0)
    {
      q1.push(p1/2);
      q2.push((p1-1)/2);
    }
    if (p2 != 0)
    {
      q1.push(p2/2);
      q2.push((p2-1)/2);
    }
  }
}

int main()
{ 
  scanf("%d", &n);
  for (int i=0; i<n; i++)
  {
    q1 = priority_queue<int>();
    q2 = priority_queue<int>();
    scanf("%d %d", &s, &k);
    insert(s/2, (s-1)/2);
    printf("Case #%d: %d %d\n", i+1, ans1, ans2);
  }
  return 0;
}
