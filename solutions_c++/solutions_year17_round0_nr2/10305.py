#include <iostream>
#include <fstream>

using namespace std;

ofstream myfile;

bool test2(int x)
{
	while(x/10)
	{
		if(x%10 < (x/10)%10)
			return false;
		x=x/10;
	}
	return true;
}

void test(int x, int n)
{
	while(x>0)
	{
		if(test2(x))
			break;
		x--;
	}
	myfile << "Case #" << n <<": " << x<<"\n";
}

void rea()
{
    ifstream read("C:\\Users\\Melih\\Desktop\\input.txt");
    int lines,x;
    read>>lines;//number of lines
    for(int i=1;i<=lines;i++)
    {
            read>>x;
            test(x,i);
    }

}

int main () {
    myfile.open ("C:\\Users\\Melih\\Desktop\\output.txt");
    rea();
    myfile.close();
    return 0;
}
