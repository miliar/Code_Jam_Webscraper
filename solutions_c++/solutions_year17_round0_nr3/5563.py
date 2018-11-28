#include "stdio.h"
#include "string.h"
#include <iostream>
#include <list>


void insertlist(std::list<int> & list, int val)
{

    std::list<int>::iterator it = list.begin();
    for (;it != list.end();++it)
    {
        if (*it < val)
        {  
            break;
        }
    }

    list.insert(it, val);
    
    return;
}

int main()
{
	using namespace std;
	FILE * finp;
	FILE * foutp;
    char buf[20];
	int t;
	
	finp = fopen("C-small-1-attempt0.in", "r");
	foutp = fopen("1.out", "w");
	fscanf(finp, "%d", &t);
	
    std::list<int> emplist;
	for (int i = 0; i<t; ++i)
	{
        int n, m;
        int rmax = 0, rmin = 0;
        int tmp = 0;
        fscanf(finp, "%d %d", &n, &m);

        emplist.push_back(n);
        for (int j = 0;j != m;++j)
        {
            tmp = *emplist.begin();
            emplist.pop_front();
            rmax = tmp / 2;
            rmin = tmp - 1 - rmax;
            insertlist(emplist, rmax);
            insertlist(emplist, rmin);
        }


        fprintf(foutp, "Case #%d: %d %d\n", i + 1, rmax, rmin);
        emplist.clear();

	}

	fclose(finp);
	fclose(foutp);
    
	return 0;
}
