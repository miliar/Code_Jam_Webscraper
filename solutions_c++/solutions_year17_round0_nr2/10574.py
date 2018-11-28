/*#include<iostream>
using namespace std;

bool checkor(long int n)
{
    // Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit < next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}
void main()
{
long int N[1000],i,T,Q;
cin>>T;
for( i=0;i<T;i++)
		cin>>N[i];
for( int j=0;j<T;j++)
	{
	//cin>>N;Q=N;
	for(long int k=N[i];k>=0; )
		{
		if(checkor(k))
		{
			cout<<k;
			break;
		}
		else
			k--;
		}
	
	}
}*/


#include<iostream>
#include<fstream>
#include<string>

using namespace std;
bool checkor(long int n)
{
// Note that digits are traversed from last to first
int next_digit = n % 10;
n = n / 10;
while (n)
{
int digit = n % 10;
if (digit > next_digit)
return false;
next_digit = digit;
n = n / 10;
}

return true;
}

void main()
{
std::streambuf *coutbuf = std::cout.rdbuf();
std::streambuf *cinbuf = std::cin.rdbuf();

std::ofstream out("outputfile.out");
std::ifstream in("B-small-attempt1.in");

//Read from infile.txt using std::std::cin
std::cin.rdbuf(in.rdbuf());

//Write to outfile.txt through std::cout
std::cout.rdbuf(out.rdbuf());

int t, n;
int q[1000], i, j, k;
cin >> t;
for (i = 0; i < t; i++)
{
cin >> q[i];
}
for (i = 0; i < t; i++)
{
for (j = q[i]; j >= 0;)
{
if (checkor(j))
{
cout << "Case #" << i + 1<<": "<<j<< endl;

break;
}
else
j--;
//checkor(j) ? cout <<j: j--;
}
}
std::cin.rdbuf(cinbuf);   //reset to standard input again
std::cout.rdbuf(coutbuf); //reset to standard output again
}

