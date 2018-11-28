#include<iostream>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
  int tc, t, i;
  string ans;
  cin >> tc;
  for (int t = 1; t <= tc; t++)
  {
  	int block = 0;
    cin >> ans;
    for (i = 0; i < ans.size() - 1; i++)
    {
      if (ans[i] > ans[i + 1]) {
      	i = block;
        ans[i] = ans[i] - 1;
        for (int j = i + 1; j < ans.size(); j++)
        {
          ans[j] = '9';
        }
        break;
      }
      
	   if(ans[i]!=ans[i+1])
      	{
      			block = i+1;
		}
    }
	if(ans[0]=='0')
	{
		string tmp="";
		for(int j=0;j<ans.size()-1;j++) tmp+='9';
		 cout << "Case #" << t << ": " << tmp << endl;
		
	}
    else cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
