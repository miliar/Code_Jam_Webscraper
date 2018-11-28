#include <iostream>
using namespace std;
#define MAX 0x7fffffff

int main()
{
    int a = -2147483647;
    int b = 2147483647;
    a--;
    b++;
    cout << a << " " << b;
	return 0;
}
