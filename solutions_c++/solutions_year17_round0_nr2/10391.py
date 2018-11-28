#include <iostream.h>
using namespace std;
void checker(int num, int no);
void main()
{
    int test_case, index = 1, test_num;
    cin >> test_case;
    while (index <= test_case)
    {
        cin >> test_num;
        checker(test_num, index);
        index++;
    }
}
void checker(int num, int no)
{
    int index = 1, r,i,j,count,tedy_num, copy;
    int p[20];
    while (index <= num)
    {
        i = 0, j = 0, count = 0;
        copy = index;
        while (copy)
        {
            r = copy % 10;
            p[i++] = r;
            p[i]=0;
            copy /= 10;
            
        }
        if(i==1)
        {
            tedy_num=index;
        }
        else
        {
        while (j < i)
        {
            if (p[j] >= p[j+1])
                count++;
                j++;
        }
        if (count == i)
        {
            tedy_num = index;
        }
        }
        index++;
    }
    cout << "Case #" << no << ": " << tedy_num << endl;
}