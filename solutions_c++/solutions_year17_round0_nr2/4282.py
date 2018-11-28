#include <bits/stdc++.h>

using namespace std;


 typedef long long ll;



//vector<vector<int> > v;

int main()
{
  int t;
  cin >>t;
 for(int k=0;k<t;k++)
  {
string s;
cin >>s;
int a[s.size()];
for(int i =0;i <s.size();i++)
{
	a[i]=int(s[i])-48;
//if(int(s[i])>int(s[i+1]))
}
for(int i =s.size()-1;i > 0;i--)
{
	
if(a[i]<a[i-1])
	{
		a[i-1]--;
		for(int j =i;j<s.size();j++)
			a[j] = 9;
		//break;
	}

}
cout <<"Case #"<<(k+1)<<": ";
for(int i =0;i <s.size();i++)
{
	if(a[i])
	cout<< a[i];

}

cout <<endl;



  }

	return 0;
}