#include <iostream>
#include <conio.h>
#include <fstream>
#include <algorithm>
using namespace std;
class loc
{
public:
	int left;
	int right;
	int count;
	int pos;
	loc()
	{
		left = 0;
		right = 0;
		count = 0;
		pos = 0;
	}
	void operator=(loc m)
	{
		right = m.right;
		left = m.left;
		count = m.count;
		pos = m.pos;
	}
};

loc dothatshit(int stalls,int n)
{
	loc temp;
	loc cmp;
	int j;
	int set = 0;
	int size = stalls + 2;
	int *arr = new int[size];
	for (int i = 0;i < size;i++)
	{
		arr[i] = 0;
	}
	arr[0] = 1;
	arr[size - 1] = 1;
	for (int i = 1;i <= n;i++)
	{
		if (set == 1)
		{
			temp.left = 0;
			temp.right = 0;
			temp.count = 0;
			cmp = temp;
			set = 0;
		}
		while (temp.right<size-1)
		{
			for (j =temp.right+1;arr[j] != 1;j++)
			{
				temp.count++;
			}
			temp.left=temp.right;
			temp.right = j;
			if ((temp.count > cmp.count) ||(temp.count==0 && cmp.count == 0))
			{
				cmp = temp;
			}
			temp.count = 0;
		}
		if (cmp.count % 2 == 0)
		{
			cmp.pos = cmp.left + (cmp.count / 2);
			arr[cmp.pos] = 1;
			set = 1;
		}
		else
		{
			cmp.pos = cmp.left + (cmp.count / 2)+1;
			arr[cmp.pos] = 1;
			set = 1;
		}
	}
	return cmp;
}
void main()
{
	int stalls = 0;
	int p = 0;
	int test=0;
	ifstream fin;
	ofstream fout;
	fin.open("C-small-1-attempt0.in", ios::in);
	fout.open("C-small-1-attempt0.out", ios::out | ios::app);
	fin >> test;
	for (int i = 1;i<=test && !fin.eof();i++)
		{
			fin >> stalls >> p;
			loc m = dothatshit(stalls,p);
			int ls = m.pos - m.left - 1;
			int rs = m.right - m.pos - 1;
			fout << "Case #" <<i<<": "<< max(ls, rs) << " "<< min(ls, rs)<<"\n";
		}
	fin.close();
	fout.close();
}
