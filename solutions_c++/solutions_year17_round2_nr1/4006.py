#include<iostream>
#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;



struct horse
{
	double k;
	double s;
	horse() {};
	horse(int kk, int ss) { k = kk; s = ss; };
};

double D;
int N;
inline double getT(horse h)//to destination
{
	return (D - h.k) / h.s;
}
inline double getC(horse h1, horse h2)//to catch
{
	return (h1.k - h2.k) / (h2.s - h1.s);
}
double solve()
{
	
	cin >> D >> N;
	map<int, int> m;
	vector<horse> h;
	for (int i = 0; i < N; i++)
	{
		int k, s;
		cin >> k >> s;
		if (m[k] == 0 || m[k] > s)m[k] = s;
	}
	for (map<int,int>::iterator a = m.begin() ;a!= m.end() ;a++)
	{
		h.push_back(horse(a->first,a->second));
	}
	reverse(h.begin(), h.end());

	double k = h[0].k;
	double s = h[0].s;
	double t = getT(h[0]);
	for (int i = 1 ; i < h.size() ; i++)
	{
		double cat = getC(h[i - 1], h[i]);

		if (h[i].s <= h[i - 1].s) {  t = getT(h[i]); }
		else if(t < cat ) {t = getT(h[i]);}
	}
	return D / t;

};



int main()
{
	int T;
	//freopen("Text.txt", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> T;
	cout.setf(ios::fixed);
	cout.precision();
	for (int tc = 1; tc <= T; tc++)
	{
		cout << "Case #" << tc << ": " << solve()<<endl;
		
		
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}