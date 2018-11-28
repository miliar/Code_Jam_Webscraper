
// from google code jam 2017 tidy numbers
// coding starts on 
// 

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

int main (int argc, char** argv)
{
    string input_file_name;
	//input_file_name = "C:/Users/Cloud Cho/Documents/computer_programming/c++/google code jam/2010/practice make it smooth.in";
	//input_file_name = "E:/computer_programming/c++/google code jam/input/tidy number 2017 qualitification.in";
	input_file_name = "E:/downloads/B-large.in";

	//ifstream givenfile ("practice make it smooth.in");
	ifstream givenfile (input_file_name);
    ofstream resultfile ("E:/downloads/B-large.out");

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
    
    int T, N;
	const long long int N_max=pow(10.0,18.0);
	long long int N_temp;
    
    int simi, burbank, van, hollywood, casenumber=0;
    int antimony, tellurium, selenium, bromine;
	int match, match_total;
	double insert_amount;
	const int first_line = 4;
	    
    string LDN, DIMN, Narray, Narraytemporary;
    vector<int> Narrayinint, Narrayinint_updated;
    char Narrayfraction;
        
	LDN = givenlines.at(0);
    T = ASCIItoInteger(LDN);
    //std::cout << T << endl;
	
	for (simi=1; simi<=T; simi++)
    {
        DIMN = givenlines.at(simi);
		long long int N_range = DIMN.length();
		//cout << "N range: " << N_range << endl;
		for (burbank=0; burbank<N_range; burbank++)
        {
            Narrayinint.push_back((int)DIMN.at(burbank) - 48);
		}
/*		
for 0th number (right to left)
	1st number (i) <= 0th number (j)
		move to 2nd number
	else
		1st number -> i-1 
			i == 0
				2nd--
					2nd (k==0)
						3rd--
					else
						k=9
							3rd (l==0)
								l = 9
			else
				i = i-1	
		0th number -> 9 
*/
		for (burbank=N_range-1; burbank>0; burbank--)
        {
            antimony = Narrayinint.at(burbank);
			tellurium = Narrayinint.at(burbank-1);
			//cout << tellurium << " vs. " << antimony << endl;
			if(antimony<tellurium)
			{
				tellurium--;
				Narrayinint.at(burbank-1) = tellurium;
				for (van = burbank; van<N_range; van++)
					Narrayinint.at(van) = 9;
			}				
		}
		//cout << DIMN << endl;
		//for (burbank=0; burbank<N_range; burbank++)
		//	cout << Narrayinint.at(burbank);
		//cout << endl;
		
		resultfile << "Case #" << simi << ": ";
		if (Narrayinint.at(0)!=0)
			for (burbank=0; burbank<N_range; burbank++)
				resultfile << Narrayinint.at(burbank);
		else if (Narrayinint.size()==1)
			for (burbank=0; burbank<N_range; burbank++)
				resultfile << Narrayinint.at(burbank);
		else
			for (burbank=1; burbank<N_range; burbank++)
				resultfile << Narrayinint.at(burbank);
		resultfile << endl;
		Narrayinint.clear();
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
