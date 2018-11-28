#include <iostream>
#include <queue>
using namespace std;



typedef pair<int, int> pii;
struct mys{
	int val;
	int left;
	int right;
	int leftBorder;
	int rightBorder;
	mys()
	{
		val					=0;
		left				=0;
		right				=0;
		leftBorder	=0;
		rightBorder	=0;
	}
	mys(int val_, int leftBorder_, int rightBorder_) :
		val(val_), left(val-leftBorder_-1), right(rightBorder_-val-1),leftBorder(leftBorder_),rightBorder(rightBorder_)
	{
	}
};
bool operator<(const mys& lhs, const mys& rhs)
{
	if (min(lhs.left, lhs.right) == min(rhs.left, rhs.right))
	{
		if (max(lhs.left, lhs.right) == max(rhs.left, rhs.right))
			return lhs.val > rhs.val;
		else
			return max(lhs.left, lhs.right) < max(rhs.left, rhs.right);
	}
	else
		return min(lhs.left, lhs.right) < min(rhs.left, rhs.right);
}

priority_queue<mys> q;
int getNum(int start, int end)
{
	return start + (end - start) / 2;
}

void constructTree(int leftBorder,int rightBorder,int k,int testnum)
{

	int currentNum = getNum(leftBorder, rightBorder);
	q.push(mys(currentNum, leftBorder, rightBorder));
	int counter = 0;
	while (!q.empty())
	{
		mys t = q.top();
		q.pop();
		counter++;
		if (counter == k)
		{
			cout << "Case #"<<testnum<<": "<<max(t.left, t.right) << " " << min(t.left, t.right) << endl;
			return;
		}
		mys next;
		if (t.right > 0)
		{
			currentNum = getNum(t.val, t.rightBorder);
			next.left = currentNum - t.val - 1;
			next.right = t.rightBorder - currentNum - 1;
			next.leftBorder = t.val;
			next.rightBorder = t.rightBorder;
			next.val = currentNum;
			q.push(next);
		}
		if (t.left > 0)
		{
			currentNum = getNum(t.leftBorder, t.val);
			next.left = currentNum - t.leftBorder - 1;
			next.right = t.val - currentNum - 1;
			next.leftBorder = t.leftBorder;
			next.rightBorder = t.val;
			next.val = currentNum;
			q.push(next);
		}

	}
	cout << "0 0" << endl;
}
void clear(std::priority_queue<mys> &qq)
{
	std::priority_queue<mys> empty;
	std::swap(qq, empty);
}
int main()
{
	int t = 1, n = 2, k = 2;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n>>k; 
		constructTree(0, n + 1, k,i);
		clear(q);
	}
}