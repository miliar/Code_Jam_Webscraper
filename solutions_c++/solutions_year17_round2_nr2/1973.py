#include <bits/stdc++.h>

using namespace std;

int r,o,y,g,b,v,n,b2,r2,y2;

string func()
{
	string ans;
	int i,val1,val2,val3,n1,n2,n3;
	vector<string >bl;
	vector<string> rl;
	vector<string> yl;
	for(i=1;i<=o;i++)
	{	
		bl.push_back("BOB");
	}
	for(i=1;i<=b-2*o;i++)
	{
		bl.push_back("B");
	}
	for(i=1;i<=g;i++)
	{	
		rl.push_back("RGR");
	}
	for(i=1;i<=r-2*g;i++)
	{
		rl.push_back("R");
	}
	for(i=1;i<=v;i++)
	{	
		yl.push_back("YVY");
	}
	for(i=1;i<=y-2*v;i++)
	{
		yl.push_back("Y");
	}

	if(bl.size()>=rl.size()&&bl.size()>=yl.size())
	{
		val1 = 1;
		val2 = 2;
		val3 = 3;
		n1 = bl.size();
		n2 = rl.size();
		n3 = yl.size();
	}
	else if(rl.size()>=bl.size()&&rl.size()>=yl.size())
	{
		val1 = 2;
		val2 = 3;
		val3 = 1;
		n1 = rl.size();
		n2 = yl.size();
		n3 = bl.size();
	}
	else
	{
		val1 = 3;
		val2 = 1;
		val3 = 2;
		n1= yl.size();
		n2 = bl.size();
		n3 = rl.size();
	}

	vector<int> vec,vec2;
	for(i=0;i<n2;i++)
		{
			vec.push_back(val1);
			vec.push_back(val2);
		}
		for(i=0;i<n1-n2;i++)
		{
			vec.push_back(val1);
			vec.push_back(val3);
		}
		int j = 0;
		for(i=0;i<n3-(n1-n2);i++)
		{
			vec2.push_back(vec[j++]);
			vec2.push_back(val3);
			vec2.push_back(vec[j++]);
		}
		for(;j<vec.size();j++)
			vec2.push_back(vec[j]);
	//cout << vec.size() << endl;
	//cout << vec2.size() << endl;

	int c1 = 0;
	int c2 = 0;
	int c3 = 0;
	for(i=0;i<vec2.size();i++)
	{
		if(vec2[i]==1)
			ans = ans+bl[c1++];
		else if(vec2[i]==2)
			ans = ans + rl[c2++];
		else
			ans = ans + yl[c3++];
	}
	return ans;
}


int main()
{
	int t,tt,sum;
	cin >> t;
	for(tt=1;tt<=t;tt++)
	{
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << tt << ": ";
		if(o<=2*b&&g<=2*r&&v<=2*y)
		{
			b2 = b-o;
			r2 = r-g;
			y2 = y-v;
			sum = b2+r2+y2;
			if(b2<=floor(sum/2.0)&&r2<=floor(sum/2.0)&&y2<=floor(sum/2.0))
			{
				if((b2==1||r2==1||y2==1)&&(sum==1))
				{	
					cout << "IMPOSSIBLE" << endl;
				}
				else
				{
					//cout << "here" << endl;
					cout << func() << endl;
				}
				
			}
			else
				cout << "IMPOSSIBLE" << endl;
		}
		else
			cout << "IMPOSSIBLE" << endl;
	}
}