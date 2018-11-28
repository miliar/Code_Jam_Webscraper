#include <istream>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <map>
#include <algorithm>
#include <sstream>
#define _USE_MATH_DEFINES
#include <math.h>
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

void calculate1(int t) {
	int N, R, O, Y, G, B, V;
	inp >> N >> R >> O >> Y >> G >> B >> V;

	int rc = R + O + V;
	int yc = Y + O + G;
	int bc = B + V + G;
	string res;
	if ((2 * rc > N) || (2 * yc > N) || (2 * bc > N))
		res = "IMPOSSIBLE";
	else {
		if ((O == 0) && (V == 0) && (G == 0)) {
			vector<pair<int, char>> V;
			V.push_back(make_pair(R, 'R'));
			V.push_back(make_pair(B, 'B'));
			V.push_back(make_pair(Y, 'Y'));
			sort(V.begin(), V.end());
			while (V[2].first > V[1].first) {
				res.push_back(V[2].second);
				res.push_back(V[1].second);
				res.push_back(V[2].second);
				res.push_back(V[0].second);
				V[2].first -= 2;
				V[1].first--;
				V[0].first--;
			}
			while (V[0].first > 0) {
				res.push_back(V[2].second);
				res.push_back(V[1].second);
				res.push_back(V[0].second);
				V[2].first--;
				V[1].first--;
				V[0].first--;
			}
			while (V[2].first > 0) {
				res.push_back(V[2].second);
				res.push_back(V[1].second);
				V[2].first--;
				V[1].first--;
			}
		}
	}

	out << "Case #" << t + 1 << ": ";
	out << res;
	out << endl;
}
class TmpC {
public:
	int r;
	int h;
	bool isAdded;
	TmpC(int a, int b) :r(a), h(b) {
		isAdded = false;
	}
};
typedef shared_ptr<TmpC> TmpCPtr;
bool comp1(TmpCPtr i, TmpCPtr j) { return (double(i->h) * i->r > double(j->h) * j->r); }
bool comp2(TmpCPtr i, TmpCPtr j) { return (i->r > j->r); }
void calculate(int t) {
	int N, K;
	inp >> N >> K;
	vector<TmpCPtr> V, R;

	for (int n = 0; n < N; n++) {
		int a, b;
		inp >> a >> b;
		TmpCPtr c = make_shared<TmpC>(a, b);

		R.push_back(c);
		V.push_back(c);
	}

	sort(V.begin(), V.end(), comp1);
	sort(R.begin(), R.end(), comp2);
	for (int i = 0; i < K-1; i++) {
		V[i]->isAdded = true;
	}
	int hr = 0;
	for (int i = 0; i < N; i++) {
		if (R[i]->isAdded) {
			hr = R[i]->r;
			break;
		}
	}
	for (int i = 0; i < N; i++) {
		if (R[i]->isAdded) {
			V[K - 1]->isAdded = true;
			break;
		}
		long long diff = (double(R[i]->r) * R[i]->r - double(hr)*hr) + 2 * double(R[i]->r) * R[i]->h;
		long long diff2 = 2 * double(V[K - 1]->r) * V[K - 1]->h;
		if (V[K - 1]->r > hr)
			diff2 += (double(V[K - 1]->r) * V[K - 1]->r - double(hr)*hr);
		if (diff > diff2) {
			R[i]->isAdded = true;
			break;
		}
		if((V[K - 1]->r == R[i]->r) && (V[K-1]->h == R[i]->h)) {
			R[i]->isAdded = true;
			break;
		}
	}
	bool isFirst = true;
	double sum = 0;
	for (int i = 0; i < N; i++) {
		if (R[i]->isAdded) {
			if (isFirst) {
				sum += double(R[i]->r) * R[i]->r;
				isFirst = false;
			}
			sum += 2 * double(R[i]->r) * R[i]->h;
		}
	}
	sum *= M_PI;

	out << "Case #" << t + 1 << ": ";
	out << fixed << sum;
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
