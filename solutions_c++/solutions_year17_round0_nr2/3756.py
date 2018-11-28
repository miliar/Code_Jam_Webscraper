#include <bits/stdc++.h>
 
#define long long long int
using namespace std;
 
#define Max 100005+5
#define cons 1000000000+7
#define mp make_pair
#define pb push_back
#define INF 1e12
#define INF2 1e9+9
#define pi 3.141592653589
#define x first
#define y second
 
 int num_string[20];
 int ans_string[20];
 int num_len ;
 int ans_len;

 bool solve(int pos,bool tight,int lastDigit)
 {
 	// cout<<pos<<" "<<tight<<" "<<lastDigit<<endl;
 	if(pos==num_len)
 	{
 		ans_len=pos;
 		return true;
 	}

 	int down_limit=lastDigit;
 	int up_limit;
 	if(tight)
 		up_limit=num_string[pos];
 	else up_limit=9;

 	if(pos!=0)
 	{
 		for(int i=up_limit;i>=down_limit;i--)
 		{
 			ans_string[pos]=i;
 			bool solved=false;
 			if(i==up_limit)
 				solved=solve(pos+1,tight,i);
 			else solved=solve(pos+1,false,i);

 			if(solved) return solved;
 		}
 	}
 	else
 	{
 		for(int i=up_limit;i>0;i--)
 		{
 			ans_string[pos]=i;
 			bool solved=false;
 			if(i==up_limit)
 				solved=solve(pos+1,tight,i);
 			else solved=solve(pos+1,false,i);

 			if(solved) return solved;
 		}
 		ans_len=num_len-1;
 		for(int i=0;i<ans_len;i++)ans_string[i]=9;
 			return true;
 	}
 	return false;
 }

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);

    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;cin>>t;
    int case_No=0;
    // cout<<t<<endl;

    while(t--)
    {
    	case_No++;   	
    	cout<<"Case #"<<case_No<<": ";

    	long n;cin>>n;
    	long copy_n=n;
    	num_len=0;
    	while(copy_n>0)
    	{
    		copy_n/=10;
    		num_len++;
    	}
    	// cout<<num_len<<endl;
    	copy_n=n;int ind=num_len-1;
    	while(copy_n>0)
    	{
    		num_string[ind--]=copy_n%10;
    		copy_n/=10;
    	}

    	solve(0,true,0);
    	for(int i=0;i<ans_len;i++)
    		cout<<ans_string[i];
    	cout<<"\n";
    }
    return 0;
}
    	