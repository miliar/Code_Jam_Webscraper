#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void)
{
	FILE *fp = fopen("Output.txt", "w+"), *fp1 = fopen("B-small-attempt3.in", "r");
	int a;
	fscanf(fp1, "%d", &a);
	for(int x=0;x<a;x++)
	{
		int n, r, o, y, g, b, v, d[6] = {0};
		char a[10000] = {0}, c[6] = {0};
		fscanf(fp1, "%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		cout<<n<<" "<<r<<" "<<o<<" "<<y<<" "<<g<<" "<<b<<" "<<v<<"\n";
		if(r>n/2||y>n/2||b>n/2)
		{
			cout<<"Case #"<<x+1<<": IMPOSSIBLE\n";
			fprintf(fp, "Case #%d: IMPOSSIBLE\n", x+1);
		}
		else
		{
			if(r>=y&&r>=b)
			{
				c[0] = 'R';
				d[0] = r;
				if(y>=b)
				{
					c[1] = 'Y';
					d[1] = y;
					c[2] = 'B';
					d[2] = b;
				}
				else
				{
					c[2] = 'B';
					d[2] = b;
					c[1] = 'Y';
					d[1] = y;
				}
			}
			else if(y>=b)
			{
				c[0] = 'Y';
				d[0] = y;
				if(r>=b)
				{
					c[1] = 'R';
					d[1] = r;
					c[2] = 'B';
					d[2] = b;
				}
				else
				{
					c[1] = 'B';
					d[1] = b;
					c[2] = 'R';
					d[2] = r;
				}
			}
			else
			{
				c[0] = 'B';
				d[0] = b;
				if(r>=y)
				{
					c[1] = 'R';
					d[1] = r;
					c[2] = 'Y';
					d[2] = y;
				}
				else
				{
					c[1] = 'Y';
					d[1] = y;
					c[2] = 'R';
					d[2] = r;
				}
			}
			cout<<c[0]<<c[1]<<c[2]<<"\n";
			cout<<d[0]<<" "<<d[1]<<" "<<d[2]<<"\n";
			for(int i=0;i<d[2]+d[1]-d[0];i++)
			{
				a[3*i] = c[0];
				a[3*i+1] = c[1];
				a[3*i+2] = c[2];
			}
			for(int i=0;i<d[0]-d[2];i++)
			{
				a[3*(d[2]+d[1]-d[0])+2*i] = c[0];
				a[3*(d[2]+d[1]-d[0])+2*i+1] = c[1];
			}
			for(int i=0;i<d[0]-d[1];i++)
			{
				a[d[2]+3*d[1]-d[0]+2*i] = c[0];
				a[d[2]+3*d[1]-d[0]+2*i+1] = c[2];
			}
			cout<<"Case #"<<x+1<<": "<<a<<"\n";
			fprintf(fp, "Case #%d: %s\n", x+1, a);
		}
	}
}
