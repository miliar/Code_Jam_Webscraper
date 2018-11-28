#include<bits/stdc++.h>
using namespace std;
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t<= test; t ++){
	int tab[2];
	tab[0] = tab[1] = 0;

	int ac, aj;
	scanf("%d %d", &ac, &aj);
	vector<pair<pair<int,int>, int> >v;
	for(int i = 0; i < ac; i ++ ){
	  int a,b;
	  scanf("%d %d", &a, &b);
	  v.push_back(make_pair(make_pair(a,b), 0));
	  tab[0] += b - a;
// 	  printf("tab[%d] + %d\n", 0, b-a);
	}
	for(int i = 0; i < aj; i ++ ){
	  int a,b;
	  scanf("%d %d", &a, &b);
	  v.push_back(make_pair(make_pair(a,b), 1));
	  tab[1] += b - a;
// 	  printf("tab[%d] + %d\n", 1, b-a);
	}
	if ( ac + aj == 0 ) {
// 	  printf("Case #%d: %d\n", t, 2);
	  continue;
	}
	
	sort(v.begin(), v.end());
	vector<pair<int,int> > z;
	int prev = v[0].first.second, exch = 0, kto = v[0].second;
	for(int i = 1; i < v.size(); i ++ ){
	  int a = v[i].first.first, b = v[i].first.second, c = v[i].second;
	  if ( kto != c ) exch ++;
	  else z.push_back(make_pair(a - prev, c));
	  kto = c;
	  prev = b;
	}
	int cykl = v[0].first.first + (1440 - prev);
	if ( v[0].second != kto ) exch ++;
	else z.push_back(make_pair(cykl, kto));
	sort(z.begin(), z.end());
	for(int i = 0; i < z.size(); i ++ ){
	  int s = z[i].first;
	  kto = abs(z[i].second);
// 	  printf("tab[%d] = %d::\n", kto, tab[kto]);
	  if ( tab[kto] + s <= 720 ){
		tab[kto] += s;
// 		printf("tab[%d] + %d\n", kto, s);
	  }
	  else {
		exch += 2;
		if ( z[i].second < 0 ) exch --;
		s -= (720-tab[kto]);
// 		printf(".. tab[%d] + %d\n", kto, 720-tab[kto]);
		tab[kto] = 720;
		tab[1-kto] += s;
// 		printf("tab[%d] + %d\n", 1-kto, s);
	  }
	}
	printf("Case #%d: %d\n", t, exch);
  }
  return 0;
}