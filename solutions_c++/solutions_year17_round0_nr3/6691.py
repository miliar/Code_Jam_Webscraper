#include <iostream>
#include <vector>

using namespace std;

struct tCase {
	int N;
	int K;
	tCase(int n, int k) : N(n), K(k) {};
};

struct Stall {
	int Ls;
	int Rs;
	bool occupied;
	Stall(int l, int r) : Ls(l), Rs(r), occupied(false) {};
	int max() {
		if (Ls > Rs) return Ls;
		else return Rs;
	}
	int min() {
		if (Ls < Rs) return Ls;
		else return Rs;
	}
};

void repair(vector<Stall> &s);
Stall lookForStall(vector<Stall> &s);
void drawStall(vector<Stall> s);

int main() {
	// Reading testcases
	int T;
	cin >> T;
	int tmpn, tmpk;
	vector<tCase> V;
	for (int i = 0; i < T; i++) {
		cin >> tmpn >> tmpk;
		tCase tmp = tCase(tmpn, tmpk);
		V.push_back(tmp);
	}

	vector<Stall> stalls;

	for (int j = 0; j < T; j++) {
		stalls.clear();
		for (int i = 0; i < V[j].N; i++)
		{
			Stall tmp = Stall(i, V[j].N - (i + 1));
			stalls.push_back(tmp);
		}
		for (int i = 0; i < V[j].K; i++)
		{
			if (i == V[j].K - 1) {
				Stall tmp = lookForStall(stalls);
				cout << "Case #" << j + 1 << ": " << tmp.max() << " " << tmp.min() << endl;
			}
			else {
				lookForStall(stalls);
			}
			repair(stalls);

		}
	}
	

	return 0;
}

void repair(vector<Stall> &s) {
	int c = 0;
	int firstind = -1;
	bool first = false;
	for (int i = 0; i < s.size(); i++) {
		if (!s[i].occupied && !first) {
			first = true;
			firstind = i;
			s[i].Ls = c;
		}
		else if (!s[i].occupied && first) {
			c++;
			s[i].Ls = c;	
		}
		else {
			if (first) {
				int tmpc = c;
				for (int j = 0; j < tmpc + 1; j++)
				{
					s[firstind].Rs = c;
					c--;
					firstind++;
				}
				
				c = 0;
			}
			first = false;
			
		}
	}
}

Stall lookForStall(vector<Stall> &s) {
	int max = -1;
	int maxind = 0;
	vector<int> indices;
	for (int i = 0; i < s.size(); i++)
	{
		if (!s[i].occupied) {
			if (s[i].min() > max) {
				indices.clear();
				max = s[i].min();
				maxind = i;
				indices.push_back(i);
			}
			else if (s[i].min() == max) {
				indices.push_back(i);
			}
		}
	}


	if (indices.size() == 1) {
		s[maxind].occupied = true;
		return s[maxind];
	}

	else {
		max = -1;
		maxind = 0;
		vector<int> newindices;
		for (int i = 0; i < indices.size(); ++i) {
			if (max < s[indices[i]].max()) {
				max = s[indices[i]].max();
				maxind = i;
				newindices.clear();
				newindices.push_back(i);
			}
			else  if (max == s[indices[i]].max()) {
				newindices.push_back(i);
			}
		}
		s[indices[newindices[0]]].occupied = true;
		return s[indices[newindices[0]]];
		
	}
}

void drawStall(vector<Stall> s) {
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i].occupied) cout << "x ";
		else cout << "o ";
	}
	cout << endl;
}