#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

typedef long long int lli;

void subtract(int *v, int i, int x){
	if (v[i] < x){
		v[i] += 10;
		subtract(v, i-1, 1);
	}
	v[i]-=x;
}

int main(){ _
	int k;
	cin >> k;
	string s;
	int v[30] = {1, 0, 2, 0, 5};
	for (int q = 1; q <= k; q++){
		cin >> s;
		int sz = s.size();
		for (int i = 0; i < sz; i++)
            v[i] = s[i] - '0';
        v[sz] = 9;
        for (int i = sz-2; i >= 0; i--){
        	while (v[i] > v[i+1]){
        		subtract(v, i, 1);
        		for (int j = i+1; j < sz; j++)
        			v[j] = 9;
        	}
        }
        cout << "Case #" << q << ": ";
        int i = 0;
        while (i < sz && v[i] == 0)
        	i++;
        while (i < sz)
        	cout << v[i++];
        cout << endl;
	}
	return 0;
}
