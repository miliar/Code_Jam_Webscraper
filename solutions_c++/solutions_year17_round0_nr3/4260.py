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

typedef v(ll) otype;
otype calcFunction(ll N, ll K) {
	ll h = ceil(log2(K+1)),
	i = K-powll(2, h-1);
	N-=1;
	ll upperN = N,
	countUpperN = 1,
	lowerN = N-1,
	countLowerN = 0;
	cout << N << " " << K << endl << h << " " << i << endl;
	/*while(h>1) {
		h--;
		if(i>=powll(2, h-1)) {
			i-=powll(2, h-1);
			N = floor((N-2)/2.);
		}
		else {
			N = ceil((N-2)/2.);
		}
		cout << N << " " << i << endl;
	}*/
	cout << "---WHILE_START---" << endl;
	while(h>1) {
		cout << h << endl;
		cout << upperN << " " << countUpperN << endl;
		cout << lowerN << " " << countLowerN << endl;
		h--;
		ll tempCntUp,
		tempCntLow;
		if(upperN%2==1 /*&& lowerN%2==0*/) {
			tempCntUp = countUpperN;
			tempCntLow = countUpperN;
			tempCntLow += 2*countLowerN;
		}
		else /*(lowerN%2==1 && upperN%2==0)*/ {
			tempCntLow = countLowerN;
			tempCntUp = countLowerN;
			tempCntUp += 2*countUpperN;
		}
		upperN = ceil((upperN-2)/2.);
		countUpperN = tempCntUp;
		lowerN = floor((lowerN-2)/2.);
		countLowerN = tempCntLow;
	}
	cout << "---WHILE_END---" << endl;
	cout << countUpperN << " " << countLowerN << endl;
	if(i < countUpperN) N=upperN;
	else N=lowerN;
	cout << N << endl;
	
	otype result;
	result.pb(ceil(N/2.));
	result.pb(floor(N/2.));
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
		//write output

		otype result=calcFunction(N, K);
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