#include <iostream>
#include <fstream>

const unsigned int LTH_N = 18;


void Input(unsigned int& T, unsigned long long*& LstN,  unsigned long long*& LstK, std::istream& In = std::cin)
{
    In >> T;

    LstN = new unsigned long long[T];
    LstK = new unsigned long long[T];
    for (unsigned int i = 0 ; i < T ; i++)
    {
        In >> LstN[i] >> LstK[i];
    }
}

void Solve(unsigned int Index, unsigned long long N, unsigned long long K, std::ostream& Out = std::cout)
{
    bool OneSpace = true;
    unsigned long long TblNbPlaces[2];
    unsigned long long TblNbEspaces[2];
    unsigned long long NewTblNbPlaces[2];
    unsigned long long NewTblNbEspaces[2];
    unsigned long long NbAPlacer = 1;
    unsigned long long y, z;

    TblNbEspaces[0] = 1;
    TblNbPlaces[0] = N;

    while (K > NbAPlacer)
    {
        if (OneSpace) // situation précédente parfaite
        {
            if ((TblNbPlaces[0] + 1) % 2 == 0) // situation actuelle parfaite
            {
                NewTblNbPlaces[0] = (TblNbPlaces[0] - 1) / 2;
                NewTblNbEspaces[0] = 2 * TblNbEspaces[0];
            }
            else // situation actuelle imparfaite
            {
                NewTblNbPlaces[0] = TblNbPlaces[0] / 2;
                NewTblNbPlaces[1] = TblNbPlaces[0] / 2 - 1;
                NewTblNbEspaces[0] = TblNbEspaces[0];
                NewTblNbEspaces[1] = TblNbEspaces[0];
                OneSpace = false;
            }
        }
        else // situation précédente imparfaite
        {
            if ((TblNbPlaces[0] + 1) % 2 == 0)
            {
                // espace grand
                NewTblNbPlaces[0] = (TblNbPlaces[0] - 1) / 2;
                NewTblNbPlaces[1] = (TblNbPlaces[0] - 1) / 2 - 1;
                NewTblNbEspaces[0] = 2 * TblNbEspaces[0];
                NewTblNbEspaces[1] = 0;

                // espace petit
                NewTblNbEspaces[0] += TblNbEspaces[1];
                NewTblNbEspaces[1] += TblNbEspaces[1];
            }
            else
            {
                // espace grand
                NewTblNbPlaces[0] = TblNbPlaces[0] / 2;
                NewTblNbPlaces[1] = TblNbPlaces[0] / 2 - 1;
                NewTblNbEspaces[0] = TblNbEspaces[0];
                NewTblNbEspaces[1] = TblNbEspaces[0];

                // espace petit
                NewTblNbEspaces[1] += 2 * TblNbEspaces[1];
            }
        }
        TblNbEspaces[0] = NewTblNbEspaces[0];
        TblNbEspaces[1] = NewTblNbEspaces[1];
        TblNbPlaces[0] = NewTblNbPlaces[0];
        TblNbPlaces[1] = NewTblNbPlaces[1];

        K -= NbAPlacer;
        NbAPlacer *= 2;
    }

    if (K <= TblNbEspaces[0])
    {
        if ((TblNbPlaces[0] - 1) % 2 == 0)
        {
            y = (TblNbPlaces[0] - 1) / 2;
            z = (TblNbPlaces[0] - 1) / 2;
        }
        else
        {
            y = TblNbPlaces[0] / 2;
            if (TblNbPlaces[0] / 2 == 0)
            {
                z = 0;
            }
            else
            {
                z = TblNbPlaces[0] / 2 - 1;
            }
        }
    }
    else
    {
        if ((TblNbPlaces[1] - 1) % 2 == 0)
        {
            y = (TblNbPlaces[1] - 1) / 2;
            z = (TblNbPlaces[1] - 1) / 2;
        }
        else
        {
            y = TblNbPlaces[1] / 2;
            if (y == 0)
            {
                z = 0;
            }
            else
            {
                z = TblNbPlaces[1] / 2 - 1;
            }
        }
    }

    Out << "Case #" << Index << ": " << y << " " << z << std::endl;
}

int main()
{
    unsigned int T;
    unsigned long long* LstN;
    unsigned long long* LstK;

    std::ifstream FileIn("C-large.in", std::ifstream::in);
    std::ofstream FileOut("out.out", std::ofstream::out);

    Input(T, LstN, LstK, FileIn);

    for (unsigned int i = 0 ; i < T ; i++)
    {
        Solve(i + 1, LstN[i], LstK[i], FileOut);
    }

    FileIn.close();
    FileOut.close();
    delete[] LstN;
    delete[] LstK;
}

