/*Divyam Goyal - IIT-BHU*/
#include<bits/stdc++.h>
using namespace std;

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)
#define MOD 1000000007
#define MAX 100005


int a[105],b[100],c[100],d[100];
int main()
{
    //ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("B-small-attempt0.in","r",stdin);freopen("output.txt","w",stdout);
    int qt;
    sd(qt);
    for(int t=1;t<=qt;t++)
    {
        printf("Case #%d: ",t);

        int ac,aj;
        cin>>ac>>aj;
        int x,y;



        for(int i=1;i<=ac;i++)
        {
        	cin>>c[i]>>d[i];
        }

        for(int i=1;i<=aj;i++)
        	cin>>a[i]>>b[i];

        if(t==15)
        {
        	trace2(ac,aj);
        	trace4(a[1],b[1],a[2],b[2]);

        }

        if(ac+aj==1){

        	if(ac)
        	{
        		x=c[1];y=d[1];
        	}
        	else
        		x=a[1];y=b[1];


        	cout<<"2"<<"\n";
			continue;
        }

        if(ac==aj)
        {

        	if(b[1]<=c[1]||d[1]<=a[1])
        		cout<<"2";
        	else
        		cout<<"4";

        	cout<<"\n";

        }
        else
        {
        	int e,f;
        	if(ac)
        	{
        		y=max(d[1],d[2]);
        		x=min(c[1],c[2]);
        		e=min(d[1],d[2]);
        		f=max(c[1],c[2]);
        	}
        	else
        	{
        		y=max(b[1],b[2]);
        		x=min(a[1],a[2]);
        		e=min(b[1],b[2]);
        		f=max(a[1],a[2]);
        	}






        	if(y-x<=720||e+f-1440<=720)
        		cout<<"2"<<"\n";
        	else
        		cout<<"4"<<"\n";
        }





    }






    return 0;


}