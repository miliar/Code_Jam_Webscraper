#include <bits/stdc++.h>
using namespace std;
int mypowerfun(int arr,int b)
{
	if(b==0)
	return 1;
	if(b==1)
	return arr;
	int x=mypowerfun( arr,b/2);
	if(b%2==0)
	return x*x;
	else
	return x*x*arr;
}
void pri_arr(int arr[],int n )
{
   int i;
   for(i=0;i<n;i++)
	  printf("%d ",arr[i]);
   printf("\n");
}
void pri_vec(vector<int> a,int n)
{
for (std::vector<int>::iterator it = a.begin() ; it != a.end(); ++it)
    std::cout  << *it;
  std::cout << '\n';
}
int mygcd(int arr,int b)
{
	if (b != 0)
       return mygcd(b, arr%b);
    else
       return arr;
}
int main()
{
    freopen("input.in","r",stdin);
freopen("output_file_name.out","w",stdout);
int t,z=1,y;
int n,k;
int result;cin>>t;
while(t--)
{
priority_queue<int>pqueue;
int run;cin>>n>>k;
pqueue.push(n);
for(int i=0;i<k-1;i++)
    {
        y=pqueue.top(); pqueue.pop();
            if(y%2!=0){pqueue.push(y/2); pqueue.push(y/2);}
            if(y%2==0){ pqueue.push(y/2); pqueue.push(y/2 - 1); }
        }
        result=pqueue.top();
        if(result%2!=0)  printf("Case #%d: %d %d\n",z,result/2,result/2);
        if(result%2==0)  printf("Case #%d: %d %d\n",z,result/2,result/2 - 1);
        z++;
    }
}
