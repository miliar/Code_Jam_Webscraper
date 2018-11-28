#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
#define ll longlong

int main(void) {
	int i, T, K;
	string S;
	scanf("%i", &T);
	for (i=0;i<T;i++) {
		cin >> S >> K;
		unsigned long int l=S.length();
		string p;
		queue <string> f;
		unordered_set <string> s; s.clear();
		vector <int> pocet; pocet.clear();
		f.push(S);
		s.insert(S);
		pocet.push_back(0);
		int prvni=0; int vysl=-1;
		while (!f.empty()) {
			p = f.front();
			f.pop();
			string h;
			for (int j=0; j<=l-K; j++) {
				h=p;
				if (h.find('-')==-1) {
					vysl=pocet[prvni];
					break;
				}
				for (int k=j; k-j<K; k++) {
					if (h[k]=='+') h[k]='-';
					else h[k]='+';
				}
				if (s.find(h) == s.end()) {
					f.push(h);
					s.insert(h);
					pocet.push_back(pocet[prvni]+1);
				}
			}
			prvni++;
		}
		if (vysl!=-1)
			printf("Case #%i: %i\n", i+1, vysl);
		else
			printf("Case #%i: IMPOSSIBLE\n",i+1);
	}
    return 0;
}
