//
// Created by pierre on 13.05.17.
//

#include <iostream>
#include <vector>

using namespace std;

int numSeats;
int numCustomers;
int numTickets;

int dasie(int s);
int seats[1009];
int customers[1009];

int main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    cin >> numSeats >> numCustomers >> numTickets;

    for (int i = 0; i < numTickets; i++)
    {
      int s, c;
      cin >> s >> c;
      s--;
      c--;
      seats[s]++;
      customers[c]++;
    }

    int p = customers[0];
    for (int i = 0; i < numCustomers; i++)
    {
      if (customers[i] > p)
        p = customers[i];
    }

    int q = numTickets;

    while (p < q)
    {
      int s = (p + q) / 2;

      if (dasie(s) >= 0)
        q = s;
      else
        p = s + 1;
    }


    cout << "Case #" << aa + 1 << ": ";
    cout << p << " " << dasie(p) << endl;

    for (int i = 0; i < numCustomers; i++)
    {
      customers[i] = 0;
    }

    for (int i = 0; i < numSeats; i++)
    {
      seats[i] = 0;
    }

  }
}

int dasie(int s)
{
  int currentUp = 0;
  int sumUp = 0;

  for (int i = numSeats - 1; i >= 0; i--)
  {
    if (seats[i] > s)
    {
      sumUp += seats[i] - s;
      currentUp += seats[i] - s;
    }

    if (seats[i] < s)
    {
      currentUp -= s - seats[i];
      currentUp = max(currentUp, 0);
    }
  }

  if (currentUp > 0)
    return -1;

  return sumUp;
}
