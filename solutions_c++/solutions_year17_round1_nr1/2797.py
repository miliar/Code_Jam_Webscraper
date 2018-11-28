// Problem_A.cpp : main project file.

#include "stdafx.h"

using namespace System;

System::String^ Test (System::IO::TextReader^ rdr);
int main(array<System::String ^> ^args)
{
#if 0
    System::Console::WriteLine ("Case #1: " + Test ("132"));
    System::Console::WriteLine ("Case #2: " + Test ("1000"));
    System::Console::WriteLine ("Case #3: " + Test ("7"));
    System::Console::WriteLine ("Case #4: " + Test ("1110"));
    System::Console::WriteLine ("Case #5: " + Test ("111111111111111110"));
    System::Console::WriteLine ("Case #6: " + Test ("1010101010"));
    System::Console::WriteLine ("Case #7: " + Test ("101010101"));
    System::Console::WriteLine ("Case #8: " + Test ("10101010110"));
/*
    Case #1: 129
    Case #2: 999
    Case #3: 7
    Case #4: 999
    Case #5: 99999999999999999
*/
#else
#if 0
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader (args[0]);
#else
    System::IO::TextReader^ rdr = System::Console::In;
#endif
    int t;
    t = System::Convert::ToInt32(rdr->ReadLine());
    for (int i = 1; i <= t; ++i)
    {
        System::Console::WriteLine ("Case #" + i.ToString() + ":" + System::Environment::NewLine + Test (rdr));
    }
#endif
    rdr->Close();
    return 0;
}

System::Char ToChar(System::Int32 v)
{
    System::Char retval = 'A'-1;
    while (v)
    {
        retval++;
        v>>=1;
    }
    return retval;
}
System::String^ Test (System::IO::TextReader^ rdr)
{
    array<System::String^>^ split = rdr->ReadLine()->Split(' ');
    System::Int32 R, C;
    R = System::Convert::ToInt32 (split[0]);
    C = System::Convert::ToInt32 (split[1]);
    array<System::String^>^ lines = gcnew array<System::String^>(R);
    for (System::Int32 i=0; i<R; i++)
        lines[i] = rdr->ReadLine();
    array<System::UInt32,2>^ Inits = gcnew array<System::UInt32,2>(R,C);
    for (System::Int32 i=0; i<R; i++)
    {
        for (System::Int32 j=0; j<C; j++)
        {
            if (lines[i][j] != '?')
            {
                Inits[i,j] = (1<<(lines[i][j]-'A'));
            }
            else
            {
                Inits[i,j] = 0;
                //if ((i>0)   && (lines[i-1][j  ] != '?')) Inits[i,j] |= (1<<(lines[i-1][j  ]-'A'));
                //if ((i<R-1) && (lines[i+1][j  ] != '?')) Inits[i,j] |= (1<<(lines[i+1][j  ]-'A'));
                //if ((j>0)   && (lines[i  ][j-1] != '?')) Inits[i,j] |= (1<<(lines[i  ][j-1]-'A'));
                //if ((j<C-1) && (lines[i  ][j+1] != '?')) Inits[i,j] |= (1<<(lines[i  ][j+1]-'A'));
                if (Inits[i,j] == 0)
                    Inits[i,j] = 0xFFFF;
            }
        }
    }
    for (System::Int32 i=0; i<R; i++)
    {
        System::UInt16 mask = 0xFFFF;
        System::Int32 j_start = 0;
        for (System::Int32 j=0; j<C; j++)
        {
            if ((mask & Inits[i,j]) == 0)
            {
                for (System::Int32 jj=j_start; jj<j; jj++)
                {
                    Inits[i,jj] &= mask;
                }
                mask = Inits[i,j];
                j_start = j;
            }
            else
            {
                mask &= Inits[i,j];
            }
        }
        for (System::Int32 jj=j_start; jj<C; jj++)
        {
            Inits[i,jj] &= mask;
        }
    }
#if 1
    for (System::Int32 j=0; j<C; j++)
    {
        System::UInt16 mask = 0xFFFF;
        System::Int32 i_start = 0;
        for (System::Int32 i=0; i<R; i++)
        {
            if ((mask & Inits[i,j]) == 0)
            {
                for (System::Int32 ii=i_start; ii<i; ii++)
                {
                    Inits[ii,j] &= mask;
                }
                mask = Inits[i,j];
                i_start = i;
            }
            else
            {
                mask &= Inits[i,j];
            }
        }
        for (System::Int32 ii=i_start; ii<R; ii++)
        {
            Inits[ii,j] &= mask;
        }
    }
#endif
    System::String^ retval = "";
    for (System::Int32 i=0; i<R; i++)
    {
        for (System::Int32 j=0; j<C; j++)
        {
            retval += ToChar(Inits[i,j]);
        }
        retval += System::Environment::NewLine;
    }
    return retval;
}
