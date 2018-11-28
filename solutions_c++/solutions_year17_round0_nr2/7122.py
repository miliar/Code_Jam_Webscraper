#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define OO 1e9
#define md 1000000007

ll str_to_int (const string &str)
{
  stringstream ss(str);
  ll num;
  if((ss >> num).fail())
  {
      //ERROR
  }
  return num;
}

ll GetNum(int st, int sz, string a, string b)
{
	string temp = a;
	for(int i=0; i< (sz-1-st); i++)
		temp+=b;
	return str_to_int(temp);
}
int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  ll t,num,mid;
  int e,s;
  string str;

  cin>>t;
  for(int tt=1; tt<=t; tt++)
  {
	  cin>>str;
	  num = str_to_int(str);
	  for(int i=0; i<str.size()-1; i++)
	  {
		  if(str[i] > str[i+1])
		  {
			e=i;
			for(int j=0; j<=e; j++)
			{
				if(str[j] == str[e])
				{
					s=j;
					break;
				}
			}
			ll s1 = GetNum(s,str.size(), "1", "0");
			num -= s1;
			mid = GetNum(s+1, str.size(), "9", "9") - str_to_int(str.substr(s+1));
			num += mid;
			break;
		  }
	  }
	  cout<<"Case #"<<tt<<": "<<num<<endl;
  }
  return 0;
}
