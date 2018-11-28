#include <cstdlib>
#include <cstdio>
#include <queue>

using namespace std;

struct Truc
{
	int left, right;
	int pos;
	
	bool operator < (const Truc& autre) const
	{
		if(min(left, right) == min(autre.left, autre.right))
		{
			if(max(left, right) == max(autre.left, autre.right))
				return pos > autre.pos;
			return max(left, right) < max(autre.left, autre.right);
		}
		return min(left, right) < min(autre.left, autre.right);
	}
};

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		
		priority_queue<Truc> file;
		Truc beg;
		beg.left=(N-1)/2;
		beg.right=(N)/2;
		beg.pos = beg.left+1;
		K--;
		file.push(beg);
		
		while(K > 0)
		{
			K--;
			Truc curr = file.top();
			file.pop();
			
			Truc new1;
			new1.left = (curr.left-1)/2;
			new1.right = (curr.left)/2;
			new1.pos = curr.pos-new1.right-1;
			
			Truc new2;
			new2.left = (curr.right-1)/2;
			new2.right = (curr.right)/2;
			new1.pos = curr.pos+new2.left+1;
			
			file.push(new1);
			file.push(new2);
		}
		
		Truc sol = file.top();
		
		printf("Case #%d: %d %d\n", t, max(sol.left, sol.right), min(sol.left, sol.right));
	}
	
	return 0;
}

