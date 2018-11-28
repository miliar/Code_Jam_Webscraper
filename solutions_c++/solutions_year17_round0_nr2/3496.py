#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    cin>>T;
    for (int t=1;t<=T;t++)
    {
    	string s;
    	cin>>s;
    	string ans = s;
    	int i;
    	for(i=1;i<ans.size(); i++)
    	{
    		if(ans[i-1] > ans[i])
    			break;
		}
		if(i < ans.size())
		{
			while(i>=2 && ans[i-2] == ans[i-1])
				i--;
			if(i==1 && ans[i-1] == '1')
				ans  = string(ans.size()-1,'9');
			else
				ans = ans.substr(0,i-1) + (char)(ans[i-1]-1) +  string(ans.size()-i,'9');
		}
    	cout<<"Case #"<<t<<": "<<ans<<'\n';
	}
    return 0;
}
