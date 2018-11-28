#include<fstream>

using namespace std;

struct num {
	int val;
	num *next;
};


void main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; i++)
	{
		num *first = new num;
		num *now = first;
		first->next = 0;
		char val[20];
		in >> val;
		int len = 0;
		first->val = val[len] -48;
		len++;
		while (val[len] !='\0')
		{
			now->next = new num;
			now = now->next;
			now->next = 0;
			now->val = val[len] - 48;
			len++;
		}
		bool t = false;
		while (!t)
		{
			t = true;
			now = first;
			while (now)
			{
				if (now->next && now->next->val < now->val)
				{
					t = false;
					now->val -= 1;
					now = now->next;
					while (now)
					{
						now->val = 9;
						now = now->next;
					}
				}
				if(t)now = now->next;
			}
		}
		while (first->val == 0 && first->next) first = first->next;
		out << "Case #" << i << ": ";
		while (first)
		{
			out << first->val;
			first = first->next;
		}
		out << endl;
	}
	
}