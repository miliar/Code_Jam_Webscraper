#include <bits/stdc++.h>
using namespace std;
const int INF = 20000000;

int solve(int bits[], int N,int sz)
{
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < sz; ++i)
  {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > sz - N)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    } 
  }

  return moves;
}

int main() {
   int t;
    scanf("%d",&t);
    int num =  t;
    while(t--){
        printf("Case #%d: ",num - t);
        string str;
        cin>>str;
        int a[1003];
        for(int i=0;i<str.size();i++){
            if(str[i]=='+')
                a[i] = 1;
            else
                a[i] = 0;
        }
        int k;
        cin>>k;
        int xx = solve(a,k,str.size());
        reverse(a,a+str.size());
        int yy = solve(a,k,str.size());
        if(xx==-1 && yy==-1)
            cout<<"IMPOSSIBLE\n";
        else
        cout << min(xx,yy) << endl;
    }
    return 0;
}
