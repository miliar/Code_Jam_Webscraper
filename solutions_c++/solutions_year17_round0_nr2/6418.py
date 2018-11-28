#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.in","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
    rf;wf;
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		string inp;
		cin>>inp;
		int flag=0;
		for(int i=1;i<inp.length();i++)
		{
			if(flag==1)
			{
				inp[i]='9';
			}
			else if(inp[i-1]>inp[i])
			{
				int temp=i-1;
				while(temp>=0 && inp[temp]==inp[i-1]) temp--;
			//	cout<<temp<<endl;
				temp++;
				inp[temp]--;
				i=temp;
				//inp[i-1]--;
				//inp[i]='9';
				flag=1;
			}
		}
		cout<<"Case #"<<test<<": ";
		int ind=(inp[0]=='0')?1:0;
		for(int i=ind;i<inp.length();i++)	cout<<inp[i];

		cout<<endl;
	}
}
