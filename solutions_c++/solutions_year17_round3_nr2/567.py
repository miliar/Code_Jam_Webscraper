#include <iostream>
#include <cassert>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef string str;

template <typename T>
ostream& operator<<(ostream& os, deque<T> vector){
	if(vector.size()==0)
		return os;
	os << vector[0];
	for(ll i=1;i<vector.size();++i)
		os << " " << vector[i];
	return os;
}

//goes through the selection possibilites of k elements of the array between begin and end,
//where between selectBegin aand selectEnd pointers to the currently selected elements are
template <typename T>
bool next_selection(T* begin, T* end, T** selectBegin, T** selectEnd){
	if(*(selectEnd-1)<end-1){
		(*(selectEnd-1))++;
		return true;
	}
	else if(selectBegin+1==selectEnd){
		*selectBegin=begin;
		return false;
	}
	else{
		bool result=next_selection(begin,end-1,selectBegin,selectEnd-1);
		*(selectEnd-1)=1+*(selectEnd-2);
		return result;
	}
}

//select from elements, indicatet by the ones "1" in the binary representation
template <typename T>
deque<T> getSelection(deque<T> elements, ll binaryRepresentationOfSelection){
	deque<T> result;
	for(ll i=0;i<elements.size();++i)
		if( (binaryRepresentationOfSelection>>i)%2 )
			result.push_back(elements[i]);
	return result;
}

//calculating faculty of n
ll facll(ll n){
	if(n)
		return n*facll(n-1);
	return 1;
}

//calculating faculty of n, floating point calulations
ld facld(ll n){
	if(n)
		return (ld)n * facld(n-1);
	return 1.;
}

//calculating the power of base to the exp
ll powll(ll base, ll exp){
	ll result=1;
	for(ll i=0;i<exp;++i)
		result*=base;
	return result;
}

#define mp make_pair
#define x first
#define y second
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define hash unordered_map
#define sz size()

#define v(type) deque<type >
#define it(container) typeof((container).begin())
#define all(x) (x).begin(), (x).end()
#define select(x,i) (x).begin()+(i), (x).begin()+(i)+1
#define foreach(cit,container) for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); cit++)
#define foreachc(c,cit,container) ll c=0;for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); c++, cit++)
#define forn(i, n) for (ll i = 0; i < (ll)(n); ++i)
#define fornn(i, a, b) for (ll i = (ll)(a); i < (ll)(b); ++i)
#define fore(i, a, b) for (ll i = (ll)(a); i <= (ll)(b); ++i)

#define inf 9000000000000000000L
#define eps 1e-15
#define pi 3.14159265358979323846264338328L

void init(){
}

typedef ll otype;
otype calcFunction(ll Ac, ll Aj, deque<pair<int, int>> C, deque<pair<int, int>> J) {
	otype result=0;
	
	int Jidx = 0;
	v(ll) timeDiffs;
	int usedTime = 0;
	int startVal, endVal;
	for(int i=0; i<Ac-1; i++) {
		startVal = C[i].second;
		endVal = C[i+1].first;
		usedTime += C[i].second - C[i].first;
		bool possible = true;
		while(Jidx != Aj && J[Jidx].first < endVal) {
			if(J[Jidx].first >= startVal) possible = false;
			Jidx++;
		}
		if(possible) {
			timeDiffs.pb(endVal - startVal);
		}
		else {
			timeDiffs.pb(1000);
		}
	}
	if(Ac > 0) {
		usedTime += C[Ac-1].second - C[Ac-1].first;
		startVal = C[Ac-1].second;
		endVal = C[0].first;
		if(Aj > 0 && (J[Aj-1].first > startVal || J[0].first < endVal)) {
			timeDiffs.pb(1000);
		}
		else {
			timeDiffs.pb(endVal+1440 - startVal);
		}
	}
	sort(timeDiffs.begin(), timeDiffs.end());
	while(timeDiffs.size() > 0 && usedTime + timeDiffs[0] <= 720) {
		usedTime += timeDiffs[0];
		timeDiffs.pop_front();
	}
	ll Cresult = timeDiffs.size()*2;
	
	int Cidx = 0;
	timeDiffs.clear();
	usedTime = 0;
	for(int i=0; i<Aj-1; i++) {
		startVal = J[i].second;
		endVal = J[i+1].first;
		usedTime += J[i].second - J[i].first;
		bool possible = true;
		while(Cidx != Ac && C[Cidx].first < endVal) {
			if(C[Cidx].first >= startVal) possible = false;
			Cidx++;
		}
		if(possible) {
			timeDiffs.pb(endVal - startVal);
		}
		else {
			timeDiffs.pb(1000);
		}
	}
	if(Aj>0) {
		usedTime += J[Aj-1].second - J[Aj-1].first;
		startVal = J[Aj-1].second;
		endVal = J[0].first;
		if(Ac > 0 && (C[Ac-1].first > startVal || C[0].first < endVal)) {
			timeDiffs.pb(1000);
		}
		else {
			timeDiffs.pb(endVal+1440 - startVal);
		}
	}
	sort(timeDiffs.begin(), timeDiffs.end());
	while(timeDiffs.size() > 0 && usedTime + timeDiffs[0] <= 720) {
		usedTime += timeDiffs[0];
		timeDiffs.pop_front();
	}
	ll Jresult = timeDiffs.size()*2;
	
	result = max(Cresult, Jresult);
	return result;
}

//#define IFSTRUCT	//remove comment on this line, to activate if-structure
int main() {
	init();
	ofstream outfile("output.txt");
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		ll Ac, Aj;
		cin >> Ac >> Aj;
		deque<pair<int, int>> C;
		deque<pair<int, int>> J;
		for(int i=0; i<Ac; i++) {
			int curS, curE;
			cin >> curS >> curE;
			C.pb(make_pair(curS, curE));
		}
		for(int i=0; i<Aj; i++) {
			int curS, curE;
			cin >> curS >> curE;
			J.pb(make_pair(curS, curE));
		}
		sort(C.begin(), C.end());
		sort(J.begin(), J.end());
		//write output

		otype result=calcFunction(Ac, Aj, C, J);
		outfile << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";
#ifndef IFSTRUCT
		outfile << result << endl;
		cout << result << endl;
#endif /*IFSTRUCT*/
#ifdef IFSTRUCT
		if(result>=0){
			outfile << result << endl;
			cout << result << endl;
		}
		else{
			str errorWord = "FALSE";
			outfile << errorWord << endl;
			cout << errorWord << endl;
		}
#endif /*IFSTRUCT*/
	}
	outfile.close();
	return 0;
}