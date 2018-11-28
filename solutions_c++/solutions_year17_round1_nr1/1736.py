#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

bool all_qs(char* p, int lo, int hi)
{
  for (int i=lo; i <= hi; i++)
    if (p[i] != '?')  {return false;}
  return true;
}

void fill(char** k, int rowlo, int rowhi, int collo, int colhi)
{
  //fill the two-D array k
  //indices go from k[rowlo..rowhi][collo..colhi] (inclusive)

  //if nothing to do, then done
  if (rowlo > rowhi || collo > colhi)  {return;}

  //find first non-? row
  int firstrow = -1; 
  for (int i=rowlo; i <= rowhi; i++)
  {
    if (!all_qs(k[i],collo,colhi))  {firstrow=i; break;}
  }

  if (firstrow == -1)
  {
    //all rows are question marks
    //since we assumed we started with something
    //it's guaranteed that there is a rectangle above the top square
    //so just fill down from the last character to the end
    for (int j=collo; j <= colhi; j++)
    {
      assert(rowlo-1 >= 0);
      char fillChar = k[rowlo-1][j]; 
      for (int z=rowlo; z <= rowhi; z++)
      {
        k[z][j] = fillChar;
      }
    }
    return;
  }
  //expand characters left and right
  int start = collo;

  char c;
  for (int i=collo; i <= colhi; i++)
  {
    if (k[firstrow][i] != '?')
    {
      c = k[firstrow][i];
      for (int j=start; j <= i; j++)
      {
        for (int z=rowlo; z <= firstrow; z++)
        {
          k[z][j] = c;
        }
      }  
      start = i+1;
    }
  }
  if (k[firstrow][colhi] == '?')
  {
    for (int j=start; j <= colhi; j++)
    {
      for (int z=rowlo; z <= firstrow; z++)
      {
        k[z][j] = c;
      }
    }
  }

  //now the first rows up to firstrow are filled
  //repeat for the rest of the cake
  fill(k, firstrow+1, rowhi, collo, colhi);
}
void solve_case()
{
  int width,height;
  cin >> width;
  cin >> height;

  char** list = new char* [width];
  for (int i=0; i < width; i++)
    list[i] = new char [height];

  for (int i=0; i < width; i++)
    for (int j=0; j < height; j++)
      cin >> list[i][j];

  fill(list, 0, width-1, 0, height-1);

  cout << endl;

  for (int i=0; i < width; i++)
  {
    for (int j=0; j < height; j++)
      cout << list[i][j];
    cout << endl;
  }

  delete [] list;
}

int main()
{
  int bigT;
  cin >> bigT;
  for (int i=1; i <= bigT; i++)
  {
    cout << "Case #" << i << ": ";
    solve_case();
  }
}
