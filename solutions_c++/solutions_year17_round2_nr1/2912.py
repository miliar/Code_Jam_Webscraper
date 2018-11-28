#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define OO 2000;
#define md 1000000007

vector<double> pos,speed;
int n,t;
double d,k,s,myT;

double getSlowest()
{
	vector<double> vec;
	for(int i=0; i<n; i++)
	{
		double tmp;
		tmp = (d - pos[i])/speed[i];
		vec.push_back(tmp);
	}
	sort(vec.begin(), vec.end());
	return vec[vec.size()-1];
}
int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  cin>>t;
  for(int tt=1; tt<=t; tt++)
  {
	  pos.clear();
	  speed.clear();

	  cin>>d>>n;
	  for(int i=0; i<n; i++)
	  {
		  cin>>k>>s;
		  pos.push_back(k);
		  speed.push_back(s);
	  }
	  myT = getSlowest();
	  cout.precision(17);
	  cout<<"Case #"<<tt<<": "<<d/myT<<endl;
  }
  return 0;
}
