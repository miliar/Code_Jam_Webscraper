#include <bits/stdc++.h>
#include<fstream>
#define li long long int
#define chal(n) for(li i=0;i<n; ++i)
#define ot(n) cout<<n<<"\n"
#define INF 1000000009
#define ld long double
#define ii pair<li, li>
using namespace std;
ii arr[1000005];
void fun()
{
    arr[1]=ii(0, 0);
    arr[2]=ii(1, 0);
    for(li i=3; i<=1000000; ++i)
    {
        li val=i-1;
        li lval=(val/2);
        li rval=val-lval;
        arr[i]=ii(max(lval, rval), min(lval, rval));
    }
}
int main()
{
    li t;
	cin>>t;
	li re=1;
	while(t--)
	{
		li n,k;		cin>>n>>k; 		k--;
		priority_queue<li> que;
		li a, b;
		que.push(n);
		while(k--)
        {
            li re=que.top();
            que.pop();
                que.push(re/2);
            if(re%2==0)
            {
                que.push((re/2)-1);
            }
            else
            {
                que.push(re/2);
            }
            if(!re)
                break;
        }    li rt=que.top();
            a=rt/2;
        if(rt%2==0)
        {
            b=rt/2-1;
        }
        else
        {
            b=rt/2;
        }
           }
        cout<<"Case #"<<re<<": "<<a<<" "<<b<<endl;
        re++;
	}
    exit(0);
}
