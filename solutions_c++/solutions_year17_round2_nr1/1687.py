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


void calculate1(int t) {
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

void calculate2(int t) {
	long long N;
	inp >> N;
	int cnt = 0;
	vector<int> A;
	long long tmp = N;
	long long ans = 1;
	while (tmp) {
		int r = tmp % 10;
		tmp = tmp / 10;
		A.push_back(r);
		cnt++;
		ans *= 10;
	}
	if (N == 0)
		ans = 0;
	else if (cnt == 1)
		ans = N;
	else {
		reverse(A.begin(), A.end());
		ans = 0;
		int c = 0;
		bool done = true;
		for (int i = 1; i < cnt; i++) {
			if (A[i] < A[i - 1]) {
				done = false;
				break;
			}
			else if (A[i] > A[i - 1]) {
				for (c; c < i; c++)
					ans = ans * 10 + A[c];
			}
		}
		if (!done) {
			ans = ans * 10 + A[c] - 1;
			c++;
			for (c; c < cnt; c++)
				ans = ans * 10 + 9;
		}
		else
			for (c; c < cnt; c++)
				ans = ans * 10 + A[c];

	}
	out << "Case #" << t + 1 << ": ";
	out << ans;
	out << endl;
}
struct TreeNode;
typedef shared_ptr<TreeNode> TreeNodePtr;
struct TreeNode {
	long max;
	TreeNodePtr left, right;
	TreeNodePtr par;
	TreeNode(TreeNodePtr p, long m):
		max(m),
		left(nullptr),
		right(nullptr),
		par(p){}
};

TreeNodePtr insertNode(TreeNodePtr root) {
	TreeNodePtr cur = root;
	while (cur->left && cur->right) {
		if (cur->right->max > cur->left->max)
			cur = cur->right;
		else
			cur = cur->left;
	}
	long max = cur->max/2;
	cur->left = make_shared<TreeNode>(cur, cur->max - max - 1);
	cur->right = make_shared<TreeNode>(cur, max);
	cur->max = max;
	TreeNodePtr ret = cur;
	cur = cur->par;
	while (cur) {
		max = cur->left->max > cur->right->max ? cur->left->max : cur->right->max;
		if (max == cur->max)
			return ret;
		cur->max = max;
		cur = cur->par;
	}
	return ret;
}

void calculate(int t) {
	int D, N;
	inp >> D >> N;
	double max = 0;
	for (int n = 0; n < N; n++) {
		long K, S;
		inp >> K >> S;
		double t = double(D - K) / S;
		if (t > max) max = t;
	}
	double val = D / max;

	out << "Case #" << t + 1 << ": ";
	out << fixed << val;
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
