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
#include <iomanip>

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

typedef ld otype;
otype calcFunction(ll N, ll K, ld U, v(ld) Ps) {
	otype result=1;
	sort(Ps.begin(), Ps.end());
	reverse(Ps.begin(), Ps.end());
	
	v(ld) interest;
	for(int i=0; i<K; i++) {
		interest.pb(Ps[i]);
	}
	
	reverse(interest.begin(), interest.end());
	ll equalIdx = 0;
	while(U > eps) {
		while(equalIdx != interest.size()-1 && (interest[equalIdx] < interest[equalIdx + 1]+eps && interest[equalIdx] > interest[equalIdx+1]-eps)) {
			equalIdx++;
		}
		//cout << U << endl;
		ld a = 0;
		if(equalIdx == interest.size()-1) {
			a = U/interest.size();
			//cout << U << endl;
		}
		else {
			ld diff = abs(interest[equalIdx+1]-interest[equalIdx]);
			if((equalIdx+1)*diff < U) {
				a = diff;
				//cout << U << endl;
			}
			else {
				a = U/(equalIdx+1);
			}
		}
		for(int i=0; i<= equalIdx; i++) {
			interest[i] += a;
		}
		U-=a*(equalIdx+1);
	}
	
	// result1:
	for(int i=0; i<K; i++) {
		result *= interest[i];
	}
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
		ll N, K;
		cin >> N >> K;
		ld U;
		cin >> U;
		v(ld) Ps;
		for(int i=0; i<N; i++) {
			ld curP;
			cin >> curP;
			Ps.pb(curP);
		}
		//write output

		otype result=calcFunction(N, K, U, Ps);
		outfile << setprecision(30);
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