#include <iostream>
#include<bits/stdc++.h>

using namespace std;

pair<int,int> solve (int n,int k){
			priority_queue <int> q;
      q.push(n);
      int counter = 0;
      int l, r;
      while(true){
      		l = 0;
          r = 0;
      		counter++;
          int temp = q.top();
          q.pop();
          if (temp > 1){
            int mid = temp / 2;
            if(mid * 2 == temp){
              q.push(mid);
              r = mid;
              if(mid > 1){
                q.push(mid-1);
                l = mid - 1;
              }
            }else{
            	l = mid;
              r = mid;
              q.push(mid);
              q.push(mid);
            }

        }
        if(counter  == k)
        	break;

      }
      return make_pair(max(l,r) , min(l,r));

}
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("oneA.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int a = 1 ; a <= t ; a++){
        int n,k;
        scanf("%d%d",&n,&k);
        pair<int,int> temp = solve(n,k);
        printf("Case #%d: %d %d\n",a,temp.first,temp.second);
    }

    return 0;
}

