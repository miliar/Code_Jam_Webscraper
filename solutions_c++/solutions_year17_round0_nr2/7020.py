// B_Tidy.cpp : main project file.

#include "stdafx.h"

using namespace System;

System::String^ Test (System::String^ str);
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
        System::Console::WriteLine ("Case #" + i.ToString() + ": " + Test (rdr->ReadLine()));
    }
#endif
    return 0;
}

System::String^ Test (System::String^ str)
{
    for (System::Int32 i=0; i<str->Length-1; i++)
    {
        if (str[i+1] < str[i])
        {
            System::Char l = str[i];
            l--;
            System::String^ nines = gcnew System::String('9', str->Length-i-1);
            str = str->Substring(0,i) + l.ToString() + nines;
            break;
        }
    }
    for (System::Int32 i=str->Length-1; i>0; i--)
    {
        if (str[i-1] > str[i])
        {
            System::Char l = str[i-1];
            l--;
            System::String^ nines = gcnew System::String('9', str->Length-i);
            str = str->Substring(0,i-1) + l.ToString() + nines;
        }
    }
    System::Int32 i=0;
    while (str[i] == '0') i++;
    return str->Substring(i);
}
