#include <bits/stdc++.h>

using namespace std;
typedef long long int lli;

int available[50][1000000];
int R[50];
int Q[50][50];

struct cppr{
	bool operator() (const pair<int, int>& a, const pair<int, int>& b)
	{
		return (a.first < b.first);
	}
} cmpre;
struct cpr{
	bool operator() (tuple<int, int, int> a, tuple<int, int, int> b)
	{
		return (get<0>(a) < get<1>(b));
	}
} cmpretple;

bool isFull(int amts[50], int N)
{
	for(int i=0;i<N;++i)
		if(amts[i] < 1)
			return false;
	return true;
}

int main()
{
	ios_base::sync_with_stdio();
	int T,N, P;
	cin >> T;
	for(int aa=1;aa<=T;++aa)
	{
		memset(available, 0, sizeof(available));
		int result = 0;
		cin >> N >> P;
		for(int i=0;i<N;++i)
			cin >> R[i];
		for(int i=0;i<N;++i)
			for(int j=0;j<P;++j)
				cin >> Q[i][j];
//		vector<pair<int, int> > ranges(N);
		vector<pair<int, int> > begins; // begin, n
		vector<pair<int, int> > ends;   // end,   n
		double dsmall, dbig;
		int smallincl, bigexcl;
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<P;++j)
			{
				dsmall = 1.0/1.1*Q[i][j]/R[i];
				dbig   = 1.0/0.9*Q[i][j]/R[i];
				dsmall -= .00000001;
				smallincl = (int) dsmall + 1;
				dbig += .00000001;
				bigexcl = (int) dbig + 1;
				//cerr << i << "," << j << ": " << smallincl << "-" << bigexcl << endl;
				if(smallincl < bigexcl)
				{
//					ranges[i].push_back(pair<int, int>(smallincl, bigexcl);
					begins.push_back(pair<int, int> (smallincl, i));
					ends.push_back(pair<int, int> (bigexcl, i));
				}
			}
		}
		sort(begins.begin(), begins.end(), cmpre);
		sort(ends.begin(), ends.end(), cmpre);
		int counts[50] = {0};
		int bit=0, eit=0;
		int pos = 0;
		int cbegin = 0;
		int cend = 0;
		int rts[50];
		while(bit!= begins.size() || eit != ends.size())
		{
			// first, find the lowest next pos;
			pos = min(begins[bit].first, ends[eit].first);
			if(eit == ends.size())
				pos = begins[bit].first;
			if(bit == begins.size())
				pos = ends[eit].first;
			//cerr << bit << " " << eit << ".  Ends.size = " << ends.size() << ", begins.size() = " << begins.size() << " : ..."  << ends[eit].first << "... "<< pos << endl;
			// now, if there's an end here, end it
			while(eit < ends.size() && (ends[eit].first == pos || ends[eit].second == -1))
			{
				if(ends[eit].second != -1)
					counts[ends[eit].second]--;
				++eit;
			}

			// now, add the positions
			while(bit < begins.size() && begins[bit].first == pos)
			{
				counts[ends[bit].second]++;
				++bit;
			}
			while(isFull(counts, N))
			{ // remove those endings and then subtract everything by 1.
				result++;
				int rmvcnt = 0;
				for(int i=0;i<N;++i)
					rts[i] = 1;
				for(int i=eit;i<ends.size() && rmvcnt < N;++i)
				{
					if(ends[i].second != -1 && rts[ends[i].second] == 1)
					{
						rts[ends[i].second] = 0;
						ends[i].second=-1;
						++rmvcnt;
					}
				}
				for(int i=0;i<N;++i)
				{
					counts[i]--;
				}
			}
		}
	
		cout << "Case #" << aa << ": " << result << endl;
	}

	return 0;
}
