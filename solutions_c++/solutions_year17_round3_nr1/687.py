#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<iomanip>

using namespace std;

#define INF 1000000000
#define ll long long
#define endl '\n'
#define double long double

const double PI = acos(-1.0);

struct Pancake
{
	double r, h;
	double side_area() const{ return 2*r*PI*h;};
	double face_area() const{ return PI*r*r; };
	Pancake(){};
	Pancake(double i, double j){r=i; h=j;};
};
inline bool operator < (const Pancake &A, const Pancake &B)
{
	if( A.side_area() != B.side_area() )
		return A.side_area() < B.side_area();	
	return A.r < B.r;
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	Pancake cake[10000];
	
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		int n,k;
		cin >> n >> k;
		
		for(int i=0; i<n; i++)
			cin >> cake[i].r >> cake[i].h;
		
		sort(cake, cake+n);
		
		double ans_area = -1;
		for(int base=0; base<n; base++)
		{	
			double base_r = cake[base].r;
			double area = cake[base].side_area()
						+ cake[base].face_area();
			
			int j=1;
			for(int i=n-1; i>=0 && j<k; i--)
			{
				if(i==base)
					continue;
				if(cake[i].r <= base_r)
				{
					area += cake[i].side_area();
					j++;
				}
			}
			
			if(j != k)
				continue;
			
			if(ans_area < area)
			{
//				cout << "base = " <<base <<endl;
				ans_area = area;
			}
		}
		
		cout << "Case #"<< t << ": "; 
		cout << fixed<< setprecision(9) << ans_area << endl;
	}
	
	return 0;
}

