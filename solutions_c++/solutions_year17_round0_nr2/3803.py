/**RootAccess IIT Madras*/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>

using namespace std;

#define INF 1000000007

bool isTidy(long long s)
{
	int last  = INF;
	while(s>0)
	{
		if(s % 10 > last)
			return false;
		last = s % 10;
		s/=10;
	}
	return true;
}

 string createTidy(long long inp, string ans)
 {
 	if(inp == 0)
 		return ans;
 	if(isTidy(inp))
 		return (to_string(inp) + ans);
 	return (createTidy(inp/10 - 1, "9" + ans));
 }
int main()
{
	int t;
	cin>>t;
	for(int cas = 1; cas<=t; cas++)
	{
		
		long long inp;
		cin>>inp;
		string ans ;
		ans.resize(19);
		ans = "";
		ans = createTidy(inp, ans);

		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
}