// A_Pancake.cpp : main project file.

#include "stdafx.h"

using namespace System;

System::String^ Test (System::String^ str);
int main(array<System::String ^> ^args)
{
#if 0
    System::Console::WriteLine ("Case #1: " + Test ("---+-++- 3"));
    System::Console::WriteLine ("Case #2: " + Test ("+++++ 4"));
    System::Console::WriteLine ("Case #3: " + Test ("-+-+- 4"));
    /*
    Case #1: 3
          ---+-++-
     111 100010110 
    Case #2: 0
    Case #3: IMPOSSIBLE
        -+-+-
        01010
        --+-+
        -+-+-        
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
        System::Console::WriteLine ("Case #" + i.ToString() + ": " + Test (rdr->ReadLine()));
    }
#endif
    return 0;
}

System::String^ Test (System::String^ str)
{
    System::String^ retval = str;
    array<System::String^>^ split = str->Split(' ');
    System::Int32 MaskLen = System::Convert::ToInt32(split[1]);
    System::Int32 moves = 0;
    for (System::Int32 i=0; i<=split[0]->Length-MaskLen; i++)
    {
        if (split[0][i] == '+') continue;
        moves++;
        for (System::Int32 j=i; j<i+MaskLen; j++)
        {
            if (split[0][j] == '-') split[0] = split[0]->Substring(0,j) + "+" + split[0]->Substring(j+1);
            else                    split[0] = split[0]->Substring(0,j) + "-" + split[0]->Substring(j+1);
        }
    }
    return split[0]->IndexOf('-')==-1?moves.ToString():"IMPOSSIBLE";
}
