#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> a;

void deletenum(int indice)
{
	if (indice>=a.size()) return;
	int p,z,r;
	z = a[indice];
	a[indice] = a[a.size()-1];
	a[a.size()-1]= z;
	a.pop_back();
	p = indice;
	while (p*2<a.size())
	{
		r = p*2;
		if ((r+1<a.size())&&(a[r+1]>a[r])) r = r+1;
		if (a[p]<a[r])
		{
			z = a[p];
			a[p] = a[r];
			a[r] = z;
			p = r;
		}
		else
			break;
	}
}

void add(int val)
{
	a.push_back(val);
	int p = a.size()-1;
	int z;
	while (p>0)
	{
		if (a[p/2]<a[p])
		{
			z = a[p];
			a[p] = a[p/2];
			a[p/2] = z;
			p = p/2;
		}
		else
			break;
	}
}

int main()
{
	ifstream in("C-small-2-attempt0.in");
	ofstream out("C-small-2-attempt0.out");
	int t;
	in >> t;
	for (int Ca=0; Ca<t; Ca++)
	{
		int n, k, m;
		in >> n >> k;
		a.clear();
		a.push_back(n);
		for (int i=0; i<k-1; i++)
		{
			m = a[0];
			deletenum(0);
			if (m&1)
			{
				if (m/2>0)
				{
					add(m/2);
					add(m/2);
				}
			}
			else
			{
				if (m/2>0) add(m/2);
				if (m/2-1>0) add(m/2-1);
			}
		}
		m = a[0];
		if (m&1)
		{
			out << "Case #" << Ca+1 << ": " << m/2 << " " << m/2 << endl;
		}
		else
		{
			out << "Case #" << Ca+1 << ": " << m/2 << " " << m/2-1 << endl;
		}
		cout << Ca+1 << "finished." << endl;
	}
	in.close();
	out.close();
	cout << "Program finished!" << endl;
	getchar();
	return 0;
}
