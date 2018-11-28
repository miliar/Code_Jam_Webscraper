
#include<bits/stdc++.h>

using namespace std;

#define ll long long

#define sci(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define scd(x) scanf("%lf",&x)

#define pfi(x) printf("%d",x)
#define pfl(x) printf("%lld",x)
#define pfd(x) printf("%lf",x)
#define pfc(x) printf("Case #%d: ",x++)
#define ps printf(" ")
#define pn printf("\n")

#define pb(x) push_back(x)
#define ppb(x) pop_back(x)
#define pf(x) push_front(x)
#define ppf(x) pop_front(x)
#define in(x,y) insert({x,y})
#define sv(a) sort(a.begin(),a.end())

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int test,caseno=1;
    sci(test);

    while(test--)
    {
        string data;
        cin>>data;
        string temp=data;
        int len=data.length();
        pfc(caseno);
        if(len==1)
        {
        	cout<<data<<endl;
        	continue;
        }
        bool done=false;
        for(int i=0;i<len;i++)
        {
        	if(data[i]=='0')
        	{
        		while(i<len && data[i]=='0')
        			i++;
        		if(i==len || data[i]!='0')
        			i--;
        		while(i>0 && (data[i]=='0'|| data[i]=='0'-1))
        		{
        			//cout<<i<<endl;
        			data[i]='9';
        			data[i-1]--;
        			i--;
        		}
        		//data[i]--;
        	}
        	//cout<<i<<' '<<data<<endl;
        	if(i<len-1 && data[i]>data[i+1] && data[i+1]!='0')
        	{
        		//cout<<i<<endl;
        		if(data[i]=='1')
        		{
        			data[i+1]='1';
        			//continue;
        		}
        		else
        		{
	        		data[i]--;
	        		data[i+1]='9';
	        	}
        	}
        	for(int j=0;j<=i;j++)
        	{
        		if(data[j]<temp[j])
        		{
        			j++;
        			while(j<len)
        			{
        				data[j]='9';
        				j++;
        			}
        			done=true;
     				break;
        		}
        	}
        	if(done)
        		break;
        }
        bool xy=false;
        while(!xy)
        {
        string t;
        for(int i=0;i<len;i++)
        {
        	if(data[i]=='0')
        		continue;
        	t+=data[i];
        }
        data=t;
        temp=data;
        len=data.length();
        done=false;
        for(int i=0;i<len;i++)
        {
        	//cout<<i<<' '<<data<<endl;
        	if(i<len-1 && data[i]>data[i+1] && data[i+1]!='0')
        	{
        		//cout<<i<<endl;
        		if(data[i]=='1')
        		{
        			data[i+1]='1';
        			//continue;
        		}
        		else
        		{
	        		data[i]--;
	        		data[i+1]='9';
	        	}
        	}
        	for(int j=0;j<=i;j++)
        	{
        		if(data[j]<temp[j])
        		{
        			j++;
        			while(j<len)
        			{
        				data[j]='9';
        				j++;
        			}
        			done=true;
     				break;
        		}
        	}
        	if(done)
        		break;
        }
        done=true;
        for(int i=0;i+1<data.length();i++)
        {
        	if(data[i]>data[i+1])
        	{
        		done=false;
        		break;
        	}
        }
        //cout<<data<<endl;
        if(done)
        {
        	xy=true;
        }
    }

        for(int i=0;i<len;i++)
        {
        	if(data[i]=='0')
        		continue;
     		cout<<data[i];
        }
        cout<<endl;
    }

    return 0;
}
