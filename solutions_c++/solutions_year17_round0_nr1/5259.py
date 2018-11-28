#include <istream>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;
#define INPFILE "input.in"
#define OUTFILE "output.out"

ifstream inp;
ofstream out;

class Linker {
public:
	Linker(int num, string nm) :mNum(num), name(nm), mParent(nullptr) {

	}
	void join(shared_ptr<Linker> par) {
		//par = par->GetParent();
		while (par->mParent) 
			par = par->mParent;
		if (mParent == nullptr)
			mParent = par;
		else {
			shared_ptr<Linker> npar = GetParent();
			npar->mParent = par;
		}
	}
	int getnum() {
		if(mParent == nullptr)
			return mNum;
		shared_ptr<Linker> npar = GetParent();
		return npar->mNum;
	}
protected:
	shared_ptr<Linker> GetParent() {
		if (mParent == nullptr)
			return nullptr;
		shared_ptr<Linker> npar = mParent;
		while (npar->mParent)
			npar = npar->mParent;
		return npar;
	}
	shared_ptr<Linker> mParent;
	int mNum;
	string name;
};

template <typename T>
struct DLLNode {
	T mVal;
	shared_ptr<DLLNode> prev, next;
	DLLNode(T val):mVal(val), prev(nullptr), next(nullptr){}
};


void calculate(int t) {
	int K;
	string S;
	inp >> S >> K;
	vector<bool> B(S.size(), false);
	for (unsigned i = 0; i < S.size(); i++) {
		if (S[i] == '+')
			B[i] = true;
	}
	int count = 0;
	bool isPossible = true;
	for (unsigned i = 0; i < B.size(); i++) {
		if (B[i]) continue;
		if (int(B.size() - i) < K) {
			isPossible = false;
			break;
		}
		count++;
		for (int j = 0; j < K; j++) {
			B[i + j] = !B[i + j];
		}
	}
	out << "Case #" << t+1 << ": ";
	if (isPossible)
		out << count;
	else
		out << "IMPOSSIBLE";
	out << endl;
}


int main() {
	int T;
	inp.open(INPFILE);
	out.open(OUTFILE);
	inp >> T;
	for (int t = 0; t < T; t++) {
		calculate(t);
	}
}
