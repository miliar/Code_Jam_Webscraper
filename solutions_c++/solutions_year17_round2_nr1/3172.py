#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>

using namespace std;
/*
template <typename T, typename Compare>
vector<size_t> sort_permutation(
    const vector<T>& vec,
    Compare& compare)
{
    vector<size_t> p(vec.size());
    iota(p.begin(), p.end(), 0);
    sort(p.begin(), p.end(),
        [&](size_t i, size_t j){ return compare(vec[i], vec[j]); });
    return p;
}

template <typename T>
vector<T> apply_permutation(
    const vector<T>& vec,
    const vector<size_t>& p)
{
    vector<T> sorted_vec(vec.size());
    transform(p.begin(), p.end(), sorted_vec.begin(),
        [&](size_t i){ return vec[i]; });
    return sorted_vec;
}*/

int main()
{
	
	unsigned nn;
	cin >> nn;
	for(unsigned kk=1; kk<=nn; kk++)
	{
		
		int D, N;
		cin >> D >> N;
		
		vector<int> K; K.reserve(N);
		vector<int> S; S.reserve(N);
		
		for(int i=0; i<N; i++)
		{
			int k, s;
			cin >> k >> s;
			if(k < D)
			{
				K.push_back(k);
				S.push_back(s);
			}
		}
		
		/*
		vector<size_t> perm = sort_permutation(K, [](int a, int b){ return a < b; });
		K = apply_permutation(K, perm);
		S = apply_permutation(S, perm);*/
		
		vector<double> T(K.size());
		for(int i=0; i<T.size(); i++)
		{
			T[i] = (double) (D - K[i]) / S[i];
		}
		
		double mt = T[0];
		for(int i=1; i<T.size(); i++)
		{
			mt = max(mt, T[i]);
		}
		
		double speed = D / mt;
		
		printf("Case #%d: %f\n", kk, speed);
	}
	
}
