#include<bits/stdc++.h>
using namespace std;

#define i3 int32_t
#define i6 int64_t
#define ui3 uint32_t
#define ui6 uint64_t
#define nl nullptr
#define rt return
#define vd void
#define mp make_pair
#define th this
typedef pair<i3, i3> pii;
typedef vector<i3> vi;

i3 d,n;
double maxd=-1;
vd input()
{
	cin>>d>>n;

	for(i3 i=0;i<n;i++)
	{
		i3 pos,h;
		double x;
		cin>>pos>>h;
		x=(double)(d-pos)/h;
		if(x>maxd) maxd=x;
	}
}

i3 main()
{
	i3 t;
	cin>>t;
	for(int ca = 1;ca<=t;ca++)
	{
		d=0;n=0;maxd=-1;
		input();
		std::cout << std::fixed << std::showpoint;
		cout<<"Case #"<<ca<<": "<<(double)d/maxd<<'\n';
	}
	return 0;
}
