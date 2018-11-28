
// from google code jam 2017 

//#include <stdafx.h> /* magic without this program won't run at prefix header */
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <iostream>
//#include <math.h>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int ASCIItoInteger (string);

class NextSection
{
      private:
              int a_n;
              int a_m;
      public:
             void seta_nanda_m(int, int);
             int changea_m();
             vector<int> insertbetween();
};

bool Read(int &x);

bool My_Read(int &x, string y);

int main ()
{
    string input_file_name;
	input_file_name = "E:/downloads/C-small-1-attempt0.in";
	ifstream givenfile (input_file_name);
    ofstream resultfile ("E:/downloads/C-small.out");

    string givenline;
    vector<string> givenlines;
    
    if (givenfile.is_open())
    {
       while (getline(givenfile,givenline))
       {
              givenlines.push_back(givenline);
       }
       givenfile.close();
    }
    else
	{
         cout << "please, check the file name or location.";
		 return -1;
	}
    
    long long int T, K, N;
	
    long long int simi, burbank, van, hollywood, casenumber=0;
    long long int antimony, tellurium, selenium, bromine_0, bromine_1;
	long long int my_min, my_max;
	int match, match_total;
	double insert_amount;
	const int first_line = 4;
	int DIMN_array[first_line];
    
    string LDN, DIMN, ikea, home, Narray, Narraytemporary;
    vector<long long int> Narrayinint, Narrayinint_updated;
	list<long long int> N_sorted;
    char Narrayfraction;
    
	T = ASCIItoInteger(givenlines.at(0));
	//cout << "T: " << T << endl;
		
	for (simi=1; simi<=T; simi++)
    {
        DIMN = givenlines.at(simi);
        antimony = DIMN.find(' ',0);
		ikea.assign(DIMN,0,antimony);
		tellurium = DIMN.find(' ',antimony+1);
		home.assign(DIMN,antimony+1,tellurium-(antimony+1));
		N = ASCIItoInteger(ikea);
		K = ASCIItoInteger(home);
		//cout << "N: " << N << " K: " << K << endl;
/*
	for i < 0 i++
		space max round up N/(2)**(i-1)
		space min round up N/(2)**(i)
*/

/*
	when add one person
		largest space 
		N-1 / 2 ?
		N
			even N/2 and N-2/2 from largest space
			odd N-1/2 and N-1/2 from largest space
			
			rearrange in size and repeat 
	I probably save result to cache to use again for large case 
*/	
		N_sorted.clear();
		N_sorted.push_back(N);
		for (burbank=0; burbank<K; burbank++)
		{
			N_sorted.sort();
			selenium=N_sorted.back();
			N_sorted.pop_back();
			if (selenium%2==0)
			{
				N_sorted.push_back(selenium/2);
				N_sorted.push_back((selenium-2)/2);
			}
			else
			{
				N_sorted.push_back((selenium-1)/2);
				N_sorted.push_back((selenium-1)/2);
			}
		}
		bromine_0 = N_sorted.back(); N_sorted.pop_back();
		bromine_1 = N_sorted.back(); N_sorted.pop_back();
		my_max = bromine_0 >= bromine_1 ? bromine_0 : bromine_1;
		my_min = bromine_0 <= bromine_1 ? bromine_0 : bromine_1;
		//cout << my_max << " " << my_min << endl;
		resultfile << "Case #" << simi << ": " << my_max << " " << my_min << endl;	
	}
    resultfile.close();
    
    //system ("pause");
    return 0;
}


int ASCIItoInteger (string temporarystring)
{
    int kip = 0, thorne = temporarystring.length();
    double bella;
    for (int nolan=0;nolan<thorne;nolan++) 
	{
        if (nolan == thorne-1) 
		{ 
            kip += (int) temporarystring.at(nolan) - 48;
        }        
        else 
		{
             bella = pow (10.0,thorne-1-nolan);
             kip += ( (int) temporarystring.at(nolan) - 48 ) * bella;
        }
             
    }
    return kip;
} 

/* only work for keyboard input somehow*/
bool Read(int &x)
{
	char c,r=0,n=0;
	x=0;
	for(;;)
	{
		c=getchar();
		if ((c<0) && (!r))
			return(0);
		if ((c=='-') && (!r))
			n=1;
		else
			if ((c>='0') && (c<='9'))
				x=x*10+c-'0',r=1;
			else
				if (r)
					break;
	}
	if (n)
		x=-x;
	return(1);
}

//bool My_Read(int &x, string y)
//{
//	char c;
//	x=0;
//	for (int i=0; i<y.length(); ++i)
//	{
//		c=str[i];
//		if ((c>='0') && (c<='9'))
//			x=x*10+c-'0',r=1;
//		else
//
//	}
//
//}
