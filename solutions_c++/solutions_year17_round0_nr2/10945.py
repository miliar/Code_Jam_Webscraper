#include<iostream>
#include<fstream>

using namespace std;

int ileCyfr (int n)
{
    int wynik;
    for (wynik = 0; n > 0; wynik++)
        n /= 10;
    return wynik;
}

void naNapis (int n, int cyfry, int * napis)
{
    for (int i = cyfry - 1; i >= 0; i--)
    {
        napis[i] = n % 10;
        n /= 10;
    }
}


int main()
{
    ifstream input;
    input.open ("0.in");
    ofstream output;
    output.open ("0.out");

    int t;
    input >> t;
    for (int j = 0; j < t; j++)
    {
        int n;
        input >> n;

        int cyfry = ileCyfr(n);
        int * napis = new int [n];
        naNapis (n, cyfry, napis);
        bool uporzadkowana = false;
        while(uporzadkowana == false)
        {
            uporzadkowana = true;
            for (int i = 1; i < cyfry; i++)
            {
                if (uporzadkowana == false)
                    napis[i] = 9;
                else
                {
                    if (napis[i-1] > napis[i])
                        {
                            napis[i-1]--;
                            napis[i] = 9;
                            uporzadkowana = false;
                        }
                }
            }
        }

        output << "Case #" << j+1 << ": ";
        int i;
        if (napis[0] == 0)
            i = 1;
        else
            i = 0;
        for (; i < cyfry; i++)
            output << napis[i];
        output << endl;
        delete [] napis;
    }
    input.close();
    output.close();
}
