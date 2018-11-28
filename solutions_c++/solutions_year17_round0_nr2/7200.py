#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long int ll;
typedef vector< pair<int,int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int,int> pii;

const ll INF= ll (1e18);
const int MOD= 1e9+7;

unsigned long long functio(string st)
{
       unsigned long long n=0,i=0;
        while(st[i]!='\0')
        {
                n=n*10+((int)st[i]-48);
                i++;
        }
        return n;
}
int main() {
    freopen("input.in","r",stdin);
freopen("output_file_name.out","w",stdout);
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
	    string nu;
	    cin>>nu;
	    int flag=0;
	    if (nu.size()==1)
	    {
	        cout<<"Case #"<<tt<<": "<<nu<<endl;
	        continue;
	    }
	    for (int i=1;i<nu.size();i++)
	    {
	    	if (nu[i]<nu[i-1])
	    	{
	    		flag=1;
	    		break;
	    	}
	    }
	    if (flag==0)
	    cout<<"Case #"<<tt<<": "<<functio(nu)<<endl;
	    else
	    {
	    	for (int i=0;i<nu.size()-1;i++)
	    	{
	    	    if (nu[i]>=nu[i+1])
	    	    {
	    	        nu[i]=nu[i]-1;
	    	        for (int j=i+1;j<nu.size();j++)
		             nu[j]='9';
		            break;
	    	    }
	    	}
	    	cout<<"Case #"<<tt<<": "<<functio(nu)<<endl;
	    }
	}
	return 0;
}
