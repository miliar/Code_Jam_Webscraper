/*
Author    : MANISH RATHI
Institute : NIT KURUKSHETRA

*******************************
Don't Stop when you are tired  *
Stop When you are Done         *
******************************* 
*/

#include<bits/stdc++.h>
using namespace std;
#define MAX 1000007
#define mode 1000000007
#define ll long long
#define ii pair<int,int>
#define vi vector<int>
#define vii vector< ii >
#define vvi vector< vi >
#define vvii vector< vii >
#define mp make_pair
#define pb push_back
#define read(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define read2(x,y) scanf("%d%d",&x,&y);
#define print2(x,y) printf("%d %d\n",x,y);
#define read_s(x) scanf("%s",x);
#define print_s(x) printf("%s",x);
#define rep(i,a,b) for(i=a;i<=b;i++)
int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("bathroom3.txt", "w", stdout);
    int t,h;
    cin>>t;
    for(h=1;h<=t;h++)
    {
    	int n,k;
    	cin>>n>>k;
    	multiset<int> myque;
    	myque.insert(0-n);
    	int maxAns,minAns;
    	for(int i=1;i<=k;i++)
    	{
    		int num= *(myque.begin());
            num= -(num);
    		myque.erase(myque.begin());
            //printf("K=%d and num=%d\n",i,num);
    		if(num&1)//odd
    		{
    			if(i==k)
    			{
    				maxAns=minAns=num/2;
    			}
    			myque.insert(-(num/2));
    			myque.insert(-(num/2));
    		}
    		else
    		{
    			if(i==k)
    			{
    				maxAns=minAns=num/2;
    				if(maxAns!=0)
                        minAns=maxAns-1;
    			}
    			myque.insert(-(num/2));
    			myque.insert(-((num/2)-1));
    		}
    	}
        if(minAns<0)
            minAns=0;
    	cout<<"Case #"<<h<<": "<<maxAns<<" "<<minAns<<endl;
    }
    return 0;
}
